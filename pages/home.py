from dash import html, register_page  #, callback # If you need callbacks, import it here.
import dash_bootstrap_components as dbc
register_page(
    __name__,
    name='Home',
    top_nav=True,
    path='/'
)


def layout():
    carousel = dbc.Carousel(
        items=[
            {
                "key": "1",
                "src": "/assets/jb.jpg",
                "header": "Auto Valuation Model",
                "caption": "Sistem Pendukung Keputusan di Jawa Barat",
                "img_style": {"width": "100%", "height": "500px"}
            },
            {
                "key": "2",
                "src": "/assets/jb2.jpg",
                "header": "Auto Valuation Model",
                "caption": "Sistem Pendukung Keputusan di Jawa Barat",
                "img_style": {"width": "100%", "height": "500px"}
            },
            {
                "key": "3",
                "src": "/assets/jb3.jpg",
                "header": "Auto Valuation Model",
                "caption": "Sistem Pendukung Keputusan di Jawa Barat",
                "img_style": {"width": "100%", "height": "500px"}
            },
        ],
        controls=True,
        indicators=True,
        interval=3000,
        ride="carousel",
    )

    layout = html.Div(children=[
        dbc.Card(
            dbc.CardBody([
                html.H2("Rekapitulasi Clustering dan Prediksi Lahan Tanah Kosong Di Jawa Barat"),
                carousel,
                html.P(
                    "Selamat datang di beranda kami! Temukan informasi terkini tentang lahan kosong di Jawa Barat. "
                    "Dapatkan wawasan tentang kondisi, tren, dan potensi pengembangan lahan ini."
                ),
                html.P(
                    "Dalam upaya untuk memfasilitasi pengambilan keputusan yang lebih cerdas dalam pengelolaan lahan, kami menyajikan analisis "
                    "mendalam yang melibatkan berbagai parameter. Melalui pemahaman "
                    "yang lebih baik terhadap data ini, diharapkan dapat membantu dalam pengembangan lahan tanah "
                    "kosong di Jawa Barat. "
                ),
                html.P(
                    "Sebagai pengguna, Anda dapat dengan mudah melihat status, grafik, dan informasi terkini tentang lahan tanah kosong di Jawa Barat melalui antarmuka yang ramah "
                    "pengguna. Dengan navigasi yang intuitif, Anda dapat menelusuri data berdasarkan kriteria tertentu, melihat prediksi perkembangan lahan, dan memahami perubahan-perubahan "
                    "yang terjadi seiring waktu. Kami berkomitmen untuk menyediakan pengalaman pengguna yang menyeluruh dan memberdayakan, memberikan alat yang diperlukan untuk pengambilan "
                    "keputusan yang lebih cerdas dalam pengelolaan lahan. Selamat menjelajahi dan memanfaatkan sumber daya informasi kami untuk mewujudkan potensi terbaik dari lahan tanah kosong "
                    "di Jawa Barat."
                    "kami juga memberikan fitur clustering dan prediksi. Dengan teknologi"
                    "canggih, kami mengelompokkan lahan-lahan dengan karakteristik serupa ke dalam cluster tertentu, memberikan gambaran yang lebih jelas tentang pola dan tren di "
                    "wilayah ini. Pengguna dapat dengan mudah menjelajahi hasil clustering untuk mendapatkan wawasan yang lebih mendalam tentang potensi dan dinamika lahan tanah kosong "
                    "di Jawa Barat.Selamat mengeksplorasi sumber daya informasi kami"
                ),
                html.P(
                    "Data ini bersumber dari KJPP Rengganis, Hamid dan Rekan. KJPP Rengganis, Hamid & Rekan (KJPP RHR) adalah firma valuation & advisory independen yang menawarkan berbagai layanan "
                    "dalam asset valuation, business valuation, consulting & advisory."
                ),
            ])
        , className="mb-4"),
        dbc.Card(
            dbc.CardBody([
                html.H2("Variabel Data dalam Dataset"),
                html.P([
                    html.B("Unnamed: 0: "), "Kolom ini mungkin adalah indeks tambahan yang disimpan pada saat DataFrame dibuat.",
                    html.Br(),
                    html.B("Tanggal Data: "), "Tanggal data tersebut dikumpulkan.",
                    html.Br(),
                    html.B("Koordinat: "), "Koordinat lokasi tertentu, disimpan sebagai string.",
                    html.Br(),
                    html.B("Kelurahan: "), "Informasi tentang kelurahan lokasi data.",
                    html.Br(),
                    html.B("Kecamatan: "), "Informasi tentang kecamatan lokasi data.",
                    html.Br(),
                    html.B("Kota/Kabupaten: "), "Informasi tentang kota/kabupaten lokasi data.",
                    html.Br(),
                    html.B("Provinsi: "), "Informasi tentang provinsi lokasi data.",
                    html.Br(),
                    html.B("LT (m2): "), "Luas tanah dalam meter persegi.",
                    html.Br(),
                    html.B("HPM: "), "Harga Properti per meter persegi.",
                    html.Br(),
                    html.B("Hak Atas Properti: "), "Informasi tentang hak atas properti tersebut.",
                    html.Br(),
                    html.B("Bentuk Tapak: "), "Informasi tentang bentuk tapak properti.",
                    html.Br(),
                    html.B("Kedudukan Tapak: "), "Informasi tentang kedudukan tapak properti.",
                    html.Br(),
                    html.B("Posisi Tapak: "), "Informasi tentang posisi tapak properti.",
                    html.Br(),
                    html.B("Kondisi Tapak: "), "Informasi tentang kondisi tapak properti.",
                    html.Br(),
                    html.B("Lebar Jalan Depan (m): "), "Lebar jalan di depan properti dalam meter.",
                    html.Br(),
                    html.B("Kondisi Wilayah Sekitar: "), "Informasi tentang kondisi wilayah sekitar properti.",
                    html.Br(),
                    html.B("Kualitas Wilayah Sekitar: "), "Informasi tentang kualitas wilayah sekitar properti.",
                    html.Br(),
                    html.B("Peruntukan: "), "Peruntukan properti.",
                    html.Br(),
                    html.B("Koordinat_pusat_kota: "), "Koordinat pusat kota.",
                    html.Br(),
                    html.B("latitude_pusatkota: "), "Latitude dari pusat kota.",
                    html.Br(),
                    html.B("longitude_pusatkota: "), "Longitude dari pusat kota.",
                    html.Br(),
                    html.B("latitude: "), "Latitude properti.",
                    html.Br(),
                    html.B("longitude: "), "Longitude properti.",
                    html.Br(),
                    html.B("distance_ke_pusatkota: "), "Jarak properti ke pusat kota.",
                    html.Br(),
                    html.B("HPM Transform: "), "HPM yang mungkin sudah diubah.",
                    html.Br(),
                    html.B("distance_ke_pusatkota Transform: "), "Jarak ke pusat kota yang mungkin sudah diubah.",
                    html.Br(),
                    html.B("Clusters: "), "Label klaster tempat properti mungkin termasuk setelah analisis klaster.",
                ])
            ])
        , className="mb-4")
    ], className="bg-light p-4 m-2")
    return layout