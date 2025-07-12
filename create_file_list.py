import pandas as pd
data = [
    {"filename": "1-s2.0-S0269749118332950-mmc1.pdf", "Type": "supplementary material"},
    {"filename": "1-s2.0-S0269749119345816-mmc1.pdf", "Type": "supplementary material"},
    {"filename": "11356_1_paper.pdf", "Type": "paper.pdf"},
    {"filename": "11356_paper.pdf", "Type": "paper.pdf"},
    {"filename": "北京市再生水补水河流中抗生素的赋存特征及生态风险评估_武亚林.pdf", "Type": "Chinese research paper"},
    {"filename":"补充材料.pdf", "Type": "supplementary material"},
    {"filename":"补充材料1.pdf", "Type": "supplementary material"},
    {"filename":"补充来料2.pdf", "Type": "supplementary material"}
]
df = pd.DataFrame(data)
df.to_excel("info/file_list.xlsx", index=False)