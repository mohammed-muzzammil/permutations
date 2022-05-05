from itertools import permutations
import pandas as pd
import streamlit as st
import os

st.title("Permutation")
temp = '/temp.csv'

# os.chdir(r'C:\Users\MOHAMMED MUZZAMMIL\Desktop\streamlit')
path = os.getcwd()
path = path + temp


def main():
    if st.button('process'):
        df1 = pd.read_csv(path)

        l = df1['Names'].tolist()

        comb = permutations(l, 2)
        comb2 = permutations(l, 2)

        df = pd.DataFrame(columns=["President", "Secretary", "Members"])
        for i in list(comb2):
            l1 = list(l)
            l1.remove(i[0])
            l1.remove(i[1])
            df = df.append({"President": i[0], "Secretary": i[1], "Members": l1}, ignore_index=True)
        print(df)
        df.to_csv(path, index=False)
        st.download_button(
            label="Download data as CSV",
            data=df.to_csv(index=False),
            file_name='permutation.csv',
            mime='text/csv',
        )


# Function to upload a csv file
def upload_file():
    uploaded_file = st.file_uploader("Upload your file", type=["csv"])
    if uploaded_file is not None:
        df1 = pd.read_csv(uploaded_file)
        df1.to_csv(path, index=False)
        st.write(df1)
        return True




upload_file()
main()
