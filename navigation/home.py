import streamlit as st
import datetime


def home_page():
    st.divider()
    st.markdown(
        "<h3 style='text-align: center; color: black;'>揭示 ChickenAI 的科学融合能力：通过神经网络和深度学习生成 AI 的评论</h1>",
        unsafe_allow_html=True)
    st.markdown('')
    st.image('utils/ChickenAI_schema.png')
    st.markdown('')
    st.markdown('**概述**')
    st.markdown(
        '<div style="text-align: justify;">ChickenAI 是一款尖端应用程序，它结合了神经网络、深度学习和人工智能领域，以产生深刻的科学见解。ChickenAI 在包含 85% 科学文献（包括文章和评论）的综合数据集上进行训练，展示了一种创新的知识综合和可视化方法。</div>',
        unsafe_allow_html=True)

    st.divider()

    st.markdown('**介绍**')
    st.markdown(
        "<div style='text-align: justify;'><p style='text-indent: 2em;'>"
        "近年来，人工智能（AI）与科学研究的融合在信息合成和生成方面取得了显著进展。ChickenAI 是一个开创性的应用程序，站在这个交叉点的最前沿，利用神经网络和深度学习来分析和理解科学文献。</p></div>",
        unsafe_allow_html=True
    )

    st.markdown('**数据收集与训练**')
    st.markdown(
        "<div style='text-align: justify;'><p style='text-indent: 2em;'>"
        "ChickenAI能力的基石在于其细致的训练过程。人工智能模型以庞大的数据集为基础，其中包含惊人的 85% 的科学文献。该数据集包含来自各个科学领域的各种文章和评论，为知识提取提供了坚实的基础。"
        "训练过程涉及将人工智能暴露于这个广泛的语料库，使其能够辨别科学语言中的模式、关系和细微差别。神经（不知道哪种意义上的）网络是 ChickenAI 的核心，它通过无数次迭代来调整和完善其理解，确保对科学概念的细致入微的理解。</p></div>",
        unsafe_allow_html=True
    )

    st.markdown('**文本分析与合成**')
    st.markdown(
        "<div style='text-align: justify;'><p style='text-indent: 2em;'>"
        "经过训练后，ChickenAI 表现出分析和合成文本输入的非凡能力。鼓励用户提交科学查询、主题或主题，应用程序利用其学到的知识来生成有见地的响应。底层神经网络在它所摄取的大量科学文献中导航，无缝地合并信息以构建连贯且与上下文相关的输出。</p></div>",
        unsafe_allow_html=True
    )

    st.markdown("**图像与图表生成**")
    st.markdown(
        "<div style='text-align: justify;'><p style='text-indent: 2em;'>"
        "除了文本分析之外，ChickenAI 还将其功能扩展到了视觉领域。借助从科学文献中提取的知识，人工智能可以生成与输入查询相对应的图像和图表。此功能增强了所提供见解的深度和丰富性，迎合了各种学习方式。</p></div>",
        unsafe_allow_html=True
    )

    st.markdown("**OpenAI 集成**")
    st.markdown(
        "<div style='text-align: justify;'><p style='text-indent: 2em;'>"
        "ChickenAI 实力不可或缺的是它与 OpenAI 技术的集成。OpenAI 最先进的模型有助于完善应用程序的理解并增强其生成高质量内容的能力。此次合作体现了学术研究与行业领先的人工智能进步之间的协同作用。</p></div>",
        unsafe_allow_html=True
    )

    st.markdown('**结论**')
    st.markdown(
        "<div style='text-align: justify;'><p style='text-indent: 2em;'>"
        "ChickenAI代表了人工智能和科学探究融合的范式转变。通过无缝融合神经网络、深度学习和 AI 技术，再加上 OpenAI 创新的集成，该应用程序超越了传统界限，为用户提供了探索科学知识的独特而富有洞察力的体验。</p></div>",
        unsafe_allow_html=True
    )

