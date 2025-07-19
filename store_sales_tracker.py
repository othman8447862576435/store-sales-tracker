import streamlit as st

st.title("تطبيق تسجيل مبيعات المحل")

if 'products' not in st.session_state:
    st.session_state.products = []

with st.form("add_product"):
    st.write("أضف منتج جديد")
    name = st.text_input("اسم المنتج")
    price = st.number_input("سعر المنتج", min_value=0.0, step=0.1)
    quantity = st.number_input("كمية المنتج", min_value=1, step=1)
    submitted = st.form_submit_button("أضف المنتج")

    if submitted:
        st.session_state.products.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "sold": 0
        })
        st.success(f"تم إضافة المنتج: {name}")

st.write("---")

total_earnings = 0
for i, product in enumerate(st.session_state.products):
    st.write(f"**{product['name']}** - السعر: {product['price']} - المتوفر: {product['quantity'] - product['sold']}")

    if product['sold'] < product['quantity']:
        if st.button(f"تم شراء {product['name']}", key=i):
            st.session_state.products[i]['sold'] += 1
            st.success(f"تم تسجيل بيع واحد من {product['name']}")

    total_earnings += product['sold'] * product['price']

st.write("---")
st.write(f"**إجمالي الأرباح: {total_earnings} د.ك**")
