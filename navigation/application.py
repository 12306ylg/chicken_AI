import pickle
import random
import time

import streamlit as st

from streamlit_searchbox import st_searchbox
from chickenAI import chickenAI


@st.cache_resource
def csl_pickle():
    with open('utils/csl.pkl', 'rb') as file:
        return pickle.load(file)


def CSL(search_citation):
    citations_returns = []
    csl = csl_pickle()

    filtered_citations = [citation for citation in csl if search_citation.lower() in citation.lower()]

    for citation in filtered_citations:
        citations_returns.append(citation)

    return citations_returns


def application_page():
    user_input = st.text_area("在此处输入您的主题：", height=200,
                              placeholder='人工智能对医疗技术演进的影响')
    if user_input:
        button = False
    else:
        button = True

    bibliography_file = st.file_uploader("上传参考书目（仅限 ZOTERO 的 CSV）", type=["csv"],
                                         help="只能用Zotero！打开Zotero，右键单击您的文件夹，导出为.csv")
    if not bibliography_file:
        bibliography_file = None

    st.subheader("生成选项")

    tab1, tab2, tab3 = st.columns(3, gap='large')

    with tab1:
        max_figures = st.slider("数字数", min_value=0, max_value=10, value=3)

        max_words = st.slider("字数", min_value=1000, max_value=10000, value=2000, step=250)

    with tab3:
        include_plots = st.checkbox("包含绘图")
        if include_plots:
            plot = True
        else:
            plot = False

        include_equations = st.checkbox("包含公式")
        if include_equations:
            equation = True
        else:
            equation = False

        generation_mode = st.radio("生成模式", ["严格", "创造"],
                                   help='严格：满足您的所有要求\n\n创造：更自由')

    with tab2:
        writing_styles = [
            "Scientific",
            "Simplification",
            "Keynote",
            "Formal Academic",
            "Journalistic",
            "Narrative",
            "Persuasive",
            "Humorous",
            "Technical",
            "Literary",
            "Popular/Informal",
            "Expository",
            "Poetic"
        ]

        writing_style = st.selectbox("写作风格", writing_styles, help='默认 Scientific')

        citation_style = st_searchbox(CSL, key="引文样式", label='引文样式（默认：Cell Research）')
        if not citation_style:
            citation_style = 'Cell Research'

    if st.button("孵化文本 🐣", use_container_width=True, disabled=button):
        with st.status("孵化中... 🐣", expanded=True) as status:
            incubator = []

            understanding = chickenAI(user_input, biblio=bibliography_file).understanding_chicken()

            analysing = chickenAI(understanding).analysing_chicken()

            style = chickenAI(analysing,
                              style=writing_style,
                              modulation=generation_mode).style_chicken()

            words = chickenAI(style,
                              figures=str(max_figures),
                              words=max_words,
                              plot=include_plots,
                              equation=include_equations).words_chicken()

            biblio = chickenAI(words,
                               citation=citation_style,
                               biblio=bibliography_file).biblio_chicken()

            citation = chickenAI(biblio,
                                 citation=citation_style,
                                 biblio=bibliography_file).citation_chicken()

            refining = chickenAI(citation,
                                 max_figures,
                                 max_words,
                                 writing_style,
                                 citation_style,
                                 generation_mode,
                                 include_plots,
                                 include_equations,
                                 bibliography_file).refining_chicken()

            incubator.append([understanding, analysing, style, words, citation, refining])

            golden_chicken = chickenAI.hatching(incubator)

            status.update(label="孵化了 ! 🐔", state="complete", expanded=False)

        st.link_button("下载你的 ChickenAI 生成 🐔", golden_chicken)

        st.balloons()
