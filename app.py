import streamlit as st
from PIL import Image
import os
import base64

st.logo("images/nocap-seal.png")

# Main Page: Grid of Images
def main_page():
    st.title('Welcome to NOCAP')
    st.image('images/nocap-seal.png', width=200)
    st.markdown('### NOCAP Apps')

    app_data = [
        {
            "app_name": "TruthScope",
            "image_url": "images/TruthScope.png",
            "url": "https://www.google.com/search?tbm=isch&q=magnifying+glass+with+an+eye+in+the+center"
        },
        {
            "app_name": "VeracityCheck",
            "image_url": "images/VeracityCheck.png",
            "url": "https://www.google.com/search?tbm=isch&q=checkmark+with+a+magnifying+glass+overlay"
        },
        {
            "app_name": "FactFinder",
            "image_url": "images/FactFinder.png",
            "url": "https://www.google.com/search?tbm=isch&q=pair+of+binoculars+with+a+document+icon"
        },
        {
            "app_name": "HonestyGauge",
            "image_url": "images/HonestyGauge.png",
            "url": "https://www.google.com/search?tbm=isch&q=speedometer+with+a+needle+pointing+to+truth"
        },
        {
            "app_name": "TransparencyTracker",
            "image_url": "images/TransparencyTracker.png",
            "url": "https://www.google.com/search?tbm=isch&q=transparent+document+with+a+tracking+arrow"
        },
        {
            "app_name": "LieSpotter",
            "image_url": "images/LieSpotter.png",
            "url": "https://www.google.com/search?tbm=isch&q=target+icon+with+a+silhouette+of+a+head"
        },
        {
            "app_name": "TruthTeller",
            "image_url": "images/TruthTeller.png",
            "url": "https://www.google.com/search?tbm=isch&q=speech+bubble+with+a+checkmark+inside"
        },
        {
            "app_name": "IntegrityLens",
            "image_url": "images/IntegrityLens.png",
            "url": "https://www.google.com/search?tbm=isch&q=lens+with+a+clear+path+leading+through+it"
        },
        {
            "app_name": "TrustVerify",
            "image_url": "images/TrustVerify.png",
            "url": "https://www.google.com/search?tbm=isch&q=handshake+icon+with+a+verification+badge"
        },
        {
            "app_name": "ClarityMonitor",
            "image_url": "images/ClarityMonitor.png",
            "url": "https://www.google.com/search?tbm=isch&q=monitor+screen+with+a+transparency+slider"
        }
    ]

    col_width = 4
    cols = st.columns(col_width, gap='medium')

    for k, i in enumerate(app_data):
        with cols[k % col_width]:
            with st.container(height=None, border=True):
                # The below is a fancy HTML way of doing this:
                # img = Image.open(i["image_url"])
                # st.image(img, use_column_width=True)
                # st.markdown(f"**{i['app_name']}**")
                # st.markdown(f"[Link]({i['url']})")

                img_base64 = base64.b64encode(open(i['image_url'], "rb").read()).decode()
                st.markdown(f'''
                    <a href="{i['url']}" target="_blank">
                        <img src="data:image/png;base64,{img_base64}" style="width:100%; height:auto; border:2px solid black; border-radius:10px;"/>
                    </a>
                    <div style="text-align:center; margin-top:10px;">
                        <a href="{i['url']}" target="_blank" style="text-decoration:none; color:lightgray">
                            <strong>{i['app_name']}</strong>
                        </a>
                    </div>
                ''', unsafe_allow_html=True)

# Mission and Vision Page: PowerPoint and Text
def mission_vision_page():
    st.title("Mission and Vision of NOCAP")

    # Display a PowerPoint slide (assuming you have a slide image)
    # ppt_image = "images/nocap-seal.png"  # Replace with the path to your PowerPoint slide image
    # st.image(ppt_image, use_column_width=True)
    st.image('images/nocap-seal.png', width=200)

    st.markdown(f"""
                ### Our Mission: To find the truth
                
Have the squad ready to prevent any beef and keep the country safe. 🛡️🇺🇸 We’re out here making sure our troops are always on point, 💪 keeping it 100 in training, 🏋️‍♂️ and being ready to roll out whenever and wherever. 🚀 We protect our turf, 🏡 handle any threats, 🚫 and make sure our allies know we got their back. 🤝 We stay on top of the latest tech, 📱💻 keeping our defenses strong and our enemies shook. 😎 So, whether it’s on land, 🏞️ sea, 🌊 or in the air, ✈️ we’re ready to flex and keep the peace. ✌️
                """)
    st.markdown(f"""### Our Vision: 🇺🇸🗽🌎💖👶
            
Ayo fam, 👋 we the peeps of the US, 🇺🇸 tryna vibe together in a lit union, ✨ making sure everything's fair and square, ⚖️ keeping it chill at home, 🏡 securing the bag for defense, 💼🛡️ promoting good vibes for everyone, 😊 and securing the glow-up for ourselves and future squad. 🔥💪🌟
                
                """)


# Team Page: Pictures and Contact Info
def team_page():
    st.title("Meet Our Team")
    st.markdown("### Our Founders")

    team = [
        {
            "name": "CAPT Storm I. Hollister (she/her/ella)",
            "image": "images/person1.png",
            "contact": "ceo@no.cap",
        },
        {
            "name": "LTC Vivi T. Castillano-Thongkham (they/them)",
            "image": "images/person2.png",
            "contact": "vtc@no.cap",
        },
        {
            "name": "Lt Col J. Lalisa 지수 Rosé-Sharma, Ph.D. (she/her)",
            "image": "images/person3.png",
            "contact": "profs@no.cap",
        },
        # Add more team members as needed
    ]

    cols = st.columns(len(team))

    for i, member in enumerate(team):
        with cols[i % len(cols)]:
            img = Image.open(member["image"])
            st.image(img, use_column_width=True)
            st.markdown(f"**{member['name']}**")
            st.markdown(f"{member['contact']}")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Mission & Vision", "Team"])

if page == "Home":
    main_page()
elif page == "Mission & Vision":
    mission_vision_page()
elif page == "Team":
    team_page()
