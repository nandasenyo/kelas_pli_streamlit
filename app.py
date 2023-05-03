import streamlit as st

st.header(':violet[Aplikasi kalkulator penjumlahan]')
st.write('Silakan input angka numerik yang ingin dihitung! :sunglasses:')

number1 = st.number_input('Masukkan bilangan pertama')
st.write(f'Bilangan pertama adalah {number1}')

number2 = st.number_input('Masukkan bilangan kedua')
st.write(f'Bilangan kedua adalah {number2}')

if number1 > 100 or number2 > 100:
	st.warning('Angka harus kecil dari 100')
elif st.button('Hitung'):
	hasil = number1 + number2
	st.success(f'Hasil penjumlahan dari {number1} + {number2} = {hasil}', icon="✅")
	st.balloons()
else:
	st.write('Silakan klik tombol "Hitung" jika kamu ingin melakukan kalkulasi')

