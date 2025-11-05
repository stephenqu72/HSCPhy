# ========================= src/auth.py =========================
import os, json, hashlib, binascii
import streamlit as st
from datetime import datetime
from src.config import ACCOUNTS_DB, USERS_ROOT

_DEF_ITER = 200_000
_DEF_ALG = "sha256"

def _new_salt():
    return binascii.hexlify(os.urandom(16)).decode()


def _hash_pw(password: str, salt: str):
    dk = hashlib.pbkdf2_hmac(_DEF_ALG, password.encode(), binascii.unhexlify(salt), _DEF_ITER)
    return binascii.hexlify(dk).decode()


def load_users():
    if not os.path.exists(ACCOUNTS_DB):
        with open(ACCOUNTS_DB, "w") as f:
            json.dump({"users": {}}, f)
        return {"users": {}}
    with open(ACCOUNTS_DB) as f:
        return json.load(f)


def save_users(db):
    with open(ACCOUNTS_DB, "w") as f:
        json.dump(db, f, indent=2)


def ensure_user_space(username):
    root = os.path.join(USERS_ROOT, username)
    os.makedirs(os.path.join(root, "feedback"), exist_ok=True)
    os.makedirs(os.path.join(root, "temp"), exist_ok=True)
    return root


def handle_auth():
    if "auth_user" not in st.session_state:
        st.session_state.auth_user = None


    with st.expander("🔐 Sign in / Sign up", expanded=st.session_state.auth_user is None):
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Login / Register"):
            db = load_users()
            user = db["users"].get(u)
            if user is None:
                salt = _new_salt()
                hash_ = _hash_pw(p, salt)
                db["users"][u] = {"salt": salt, "hash": hash_, "created": datetime.utcnow().isoformat() + "Z"}
                save_users(db)
                ensure_user_space(u)
                st.session_state.auth_user = u
                st.success("✅ Registered & Logged in!")
            else:
                calc = _hash_pw(p, user["salt"])
                if calc == user["hash"]:
                    ensure_user_space(u)
                    st.session_state.auth_user = u
                    st.success("✅ Logged in")
                else:
                    st.error("Wrong password")


    if st.session_state.auth_user:
        st.sidebar.success(f"Signed in as {st.session_state.auth_user}")
        if st.sidebar.button("Sign out"):
            st.session_state.auth_user = None
            st.rerun()
        return st.session_state.auth_user


    return None