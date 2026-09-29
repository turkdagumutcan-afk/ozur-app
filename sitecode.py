import streamlit as st

# Sayfa ayarı
st.set_page_config(page_title="Zeynep...", page_icon="❤️", layout="centered")

# Kaç kez hayır'a basıldığını hafızada tutma (State)
if "hayir_sayisi" not in st.session_state:
    st.session_state.hayir_sayisi = 0

if "baristik_mi" not in st.session_state:
    st.session_state.baristik_mi = False

# "Hayır" dendikçe çıkacak esprili ikna cümleleri
hayir_mesajlari = [
    "Zeynep gerçekten hayır mı? Emin misin? 🥺",
    "Bir daha düşün lütfen... Kalbimi kırıyorsun 💔",
    "Ama ben seni çok seviyorum, yapma böyle... 🧸",
    "Bak son şansın, affet beni ne olur! 😭",
    "Lütfen lütfen lütfen affet? 🙏",
    "Görüyorsun, Hayır butonu bile küçülüyor, kaçış yok! 😤"
]

# Eğer EVET'e basıldıysa kutlama ekranı
if st.session_state.baristik_mi:
    st.balloons()
    st.snow()
    st.title("YAAA BİLİYORDUM! ❤️🎉")
    st.subheader("İyi ki varsın Zeynep, seni çok seviyorum! 🥰✨")
    st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1eHQzM2d4N3FxeTN5ZTF0bnJ5bDF0NnB3N2VnNHp6dnFwdzJ4MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/artj92V8o75VPL7AeQ/giphy.gif",
        use_container_width=True
    )
    if st.button("Başa Dön 🔄"):
        st.session_state.hayir_sayisi = 0
        st.session_state.baristik_mi = False
        st.rerun()

else:
    # EN ÜST BAŞLIK KISMI
    st.title("❤️ ZEYNEP BENİ LÜTFEN AFFET 🥺")
    st.subheader("Benimle barışır mısın?")
    
    # Hayır dendikçe değişen sevimli gifler
    if st.session_state.hayir_sayisi == 0:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHRra2Rtcndnb3ZqOGZpdW5vbjh4ZnRwZXRjMDNqbmN0YTFueG1mMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cLS1cfxvGOPVpf9g3y/giphy.gif", width=320)
    else:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWNjcXZiOGM1dWVxZ3c3ZTF0MW4waTVwdWdudHB0MnNjcW0xZmptMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ISOckXUybVfQ4/giphy.gif", width=320)

    # Hayır dendiğinde çıkan uyarı mesajı
    if st.session_state.hayir_sayisi > 0:
        mesaj_index = min(st.session_state.hayir_sayisi - 1, len(hayir_mesajlari) - 1)
        st.warning(hayir_mesajlari[mesaj_index])

    # Hayır dendikçe EVET butonunu devasa büyüten CSS
    font_size = 18 + (st.session_state.hayir_sayisi * 14)
    padding_y = 10 + (st.session_state.hayir_sayisi * 6)
    padding_x = 24 + (st.session_state.hayir_sayisi * 10)

    st.markdown(f"""
        <style>
        div[data-testid="column"]:nth-of-type(1) button {{
            font-size: {font_size}px !important;
            padding: {padding_y}px {padding_x}px !important;
            background-color: #ff4b4b !important;
            color: white !important;
            border-radius: 12px !important;
            border: none !important;
            width: 100% !important;
            transition: all 0.2s ease-in-out;
        }}
        div[data-testid="column"]:nth-of-type(2) button {{
            background-color: #6c757d !important;
            color: white !important;
            border-radius: 10px !important;
        }}
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1 + (st.session_state.hayir_sayisi * 0.4), 1])

    with col1:
        if st.button("EVET, AFFETTİM! ❤️"):
            st.session_state.baristik_mi = True
            st.rerun()

    with col2:
        if st.button("Hayır... 💔"):
            st.session_state.hayir_sayisi += 1
            st.rerun()
