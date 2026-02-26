import streamlit as st
import pandas as pd

st.title("📂 Excel 轉 CSV 工具")
st.write("上傳 Excel 檔案，系統會**自動刪除前兩行**，並轉換成 CSV 讓你下載。")

uploaded_file = st.file_uploader("請選擇 Excel 檔案 (.xlsx 格式)", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # 讀取並刪除前兩行
        df = pd.read_excel(uploaded_file, skiprows=2)
        st.success("✅ 檔案處理成功！預覽如下：")
        st.dataframe(df.head()) # 顯示前幾行資料
        
        # 轉成 CSV 格式
        csv = df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
        
        # 下載按鈕
        st.download_button(
            label="⬇️ 點擊下載 CSV 檔案",
            data=csv,
            file_name="處理完成.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"發生錯誤：{e}")
