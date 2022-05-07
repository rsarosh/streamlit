# IMPORTING LIBRARIES
import os
import streamlit as st
import asyncio
#https://frankie567.github.io/httpx-oauth/oauth2/
from httpx_oauth.clients.google import GoogleOAuth2
from dotenv import load_dotenv

load_dotenv('.env')

client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
redirect_uri = os.environ['REDIRECT_URI']
client = GoogleOAuth2(client_id, client_secret)
 
async def get_authorization_url(client,redirect_uri):
    authorization_url = await client.get_authorization_url(redirect_uri,scope=["profile", "email"])
    return authorization_url   

async def get_access_token(client,redirect_uri,code):
    token = await client.get_access_token(code, redirect_uri)
    
    return token
 
async def get_email(client,token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email

def get_login_str():
    authorization_url = asyncio.run(get_authorization_url(client,redirect_uri))
    return f''' 
    <a target="_self"
    href="{authorization_url}">Google login</a>'''
    
    
def display_user():
    code = st.experimental_get_query_params()['code'] # get the code from the url
    token = asyncio.run(get_access_token(client, redirect_uri, code))
    user_id, user_email = asyncio.run(get_email(client, token['access_token']))
    st.write(f"You're logged in as {user_email} and id is {user_id}")
    
    