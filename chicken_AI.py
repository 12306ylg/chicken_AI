import hydralit_components as hc
import streamlit as st
import streamlit_analytics
from streamlit_modal import Modal
import streamlit_lottie
import time
import json

from utils.components import footer_style, footer
from navigation.home import home_page
from navigation.application import application_page
import os


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


st.set_page_config(
    page_title='ChickenAI',
    page_icon="utils/chicken.png",
    initial_sidebar_state="expanded"
)

if 'lottie' not in st.session_state:
    st.session_state.lottie = False

if not st.session_state.lottie:
    lottfinder = load_lottiefile("utils/ChickenAI.json")
    st.lottie(lottfinder, speed=1.3, loop=False)
    time.sleep(2)
    st.session_state.lottie = True
    st.rerun()

max_width_str = f"max-width: {75}%;"

st.markdown(f"""
        <style>
        .appview-container .main .block-container{{{max_width_str}}}
        </style>
        """,
            unsafe_allow_html=True,
            )

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;

                }
        </style>
        """, unsafe_allow_html=True)

# Footer

st.markdown(footer_style, unsafe_allow_html=True)

# NavBar

HOME = 'Home'
APPLICATION = 'ChickenAI'

tabs = [
    HOME,
    APPLICATION
]

option_data = [
    {'icon': "🏠", 'label': HOME},
    {'icon': "🤖", 'label': APPLICATION}

]

over_theme = {'txc_inactive': 'black', 'menu_background': '#F5B7B1', 'txc_active': 'white', 'option_active': '#CD5C5C'}
font_fmt = {'font-class': 'h3', 'font-size': '50%'}

chosen_tab = hc.option_bar(
    option_definition=option_data,
    title='',
    key='PrimaryOptionx',
    override_theme=over_theme,
    horizontal_orientation=True)

if chosen_tab == HOME:
    home_page()

elif chosen_tab == APPLICATION:
    application_page()

for i in range(4):
    st.markdown('#')
st.markdown(footer, unsafe_allow_html=True)

streamlit_analytics.start_tracking()

modal = Modal(key='ChickenAI', title="使用条款 - ChickenAI", padding=50, max_width=900)

if 'popup_closed' not in st.session_state:
    st.session_state.popup_closed = False

if not st.session_state.popup_closed:
    with modal.container():
        st.expander("欢迎").markdown(
            '欢迎来到 ChickenAI，在这里，创新与羽毛相遇。访问和使用本网站，即表示您同意以下条款：')
        st.expander("内容完整性：").markdown('<strong>内容完整性</strong>：提供的信息'
                    'ChickenAI 经过精心策划，以模仿真正的科学话语。尽管我们<br>努力实现'
                    '准确，这个平台是为教育和娱乐目的而设计的。任何相关性实际的科学发现纯粹是偶然的。</br>', unsafe_allow_html=True)
        st.expander("信息准确性：").markdown(
            '我们努力以最精确的方式呈现信息，但我们不能保证内容的绝对准确性或<br>适用性。'
            '请将 ChickenAI 视为一个发人深省的探索，而不是权威来源。</br>', unsafe_allow_html=True)
        st.expander("负责任的用户行为：").markdown(
            '您与 ChickenAI 的互动应以负责任的方式进行。'
            ' 严禁任何滥用、未经授权的访问或<br>试图破译隐藏的与鸡相关的隐喻。</br>', unsafe_allow_html=True)
        st.expander("数据安全：").markdown('我们非常重视您的数据安全。'
                    '所提供的所有信息均以最大程度的保密方式处理。'
                    '然而，在<br>广阔的数字合作社中，没有一个系统可以完全不受影响。</br>', unsafe_allow_html=True)
        st.expander("责任限制：").markdown('对于您使用 ChickenAI 的后果，我们不承担任何责任。 '
                    '这包括但不限于直接、<br>间接或后果性损害。如有任何疑问，请咨询我们的支持团队。</br>', unsafe_allow_html=True)
        st.expander("条款修改: ").markdown('我们保留修改这些条款的权利，恕不另行通知。 '
                    '您继续使用 ChickenAI 即表示您接受<br>更新后的条款。定期检查是否有更改。</br>', unsafe_allow_html=True)
        value = st.checkbox("点击即表示您确认已查看并接受这些条款。享受您在 ChickenAI 世界中的探索。")
        if value:
            close = st.button('关闭')
            st.session_state.popup_closed = True

st.sidebar.image("utils/ChickenAI.png",width=500)

with st.sidebar:
    st.title("Welcome to ChickenAI!")
    st.markdown(
        "ChickenAI 是一个利用神经网络、深度学习和人工智能（包括 OpenAI 技术）的高级平台。它不仅可以分析文本，还可以根据您的输入生成图像和图表。 "
        "输入您的研究主题，让 ChickenAI 孵化出深刻的见解和视觉效果，所有这些都由尖端 AI 提供支持！"
    )

streamlit_analytics.stop_tracking()
views = streamlit_analytics.main.counts["total_pageviews"]
st.sidebar.markdown(f"Total connections 👨🏼‍💻: {int(views)}")
