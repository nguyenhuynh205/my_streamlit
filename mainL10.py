import streamlit as st

st.header("Trà sữa CoTAI")
col1, col2 = st.columns(2)
with col1:
    st.image("https://i.imgur.com/lEpdPsT.jpeg")

with col2:
    size = st.radio("Chọn kích cỡ", ["Nhỏ (30K)", "Vừa (40K)", "Lớn (50K)"], horizontal = True)
    # ["Sữa (5K)", "Cà Phê (8K)", "Kem (10K)", "Trứng (15K)"]
    col1, col2 = st.columns(2)
    with col1:
        Milk = st.checkbox("Sữa (5K)")
        Coffee = st.checkbox("Cà Phê (8K)")
    with col2:
        IC = st.checkbox("Kem (10K)")
        Egg = st.checkbox("Trứng (15K)")

col3, col4 = st.columns(2)
with col3:
    Toppings = st.multiselect("Topping",["Trân châu trắng (5K)", "Trân châu đen (5K)", "Thạch rau câu (6K)", "Vải (7K)", "Nhãn (8K)", "Đào (10K)"])

with col4:
    num = st.number_input("Số lượng", 1)

note = st.text_area("Ghi Chú")

if st.button('OK', use_container_width=True):

    total = 0
    #Size
    Size_prices = {"Nhỏ (30K)": 30, "Vừa (40K)": 40, "Lớn (50K)": 50}

    total += Size_prices[size]

    Extra_prices = {"Sữa (5K)": 5, "Cà Phê (8K)": 8, "Kem (10K)": 10, "Trứng (15K)": 15}

    if Milk: total += Extra_prices["Sữa (5K)"]
    if Coffee: total += Extra_prices["Cà Phê (8K)"]
    if IC: total += Extra_prices["Kem (10K)"]
    if Egg: total += Extra_prices["Trứng (15K)"]

    Toppings_prices = {"Trân châu trắng (5K)": 5, "Trân châu đen (5K)": 5, "Thạch rau câu (6K)": 6, "Vải (7K)": 7, "Nhãn (8K)": 8, "Đào (10K)": 10}

    for topping in Toppings:
        total += Toppings_prices[topping]

    total *= num

    size_format = {"Nhỏ (30K)": "Cỡ nhỏ", "Vừa (40K)": "Cỡ vừa", "Lớn (50K)": "Cỡ lớn"}
    extra_format = []
    if Milk: extra_format.append("Sữa")
    if Coffee: extra_format.append("Cà Phê")
    if IC: extra_format.append("Kem")
    if Egg: extra_format.append("Trứng")

    extra_str = ", ".join(extra_format)
    toppings_str = ", ".join(Toppings)

    DonHang = f"{size_format[size]} \nThêm: {extra_str} \nTopping: {toppings_str} \nSố Lượng: {num} \nThành tiền: {total} *Ghi Chú: {note}"

    st.text_area("Đơn hàng", DonHang)