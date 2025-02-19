<?php
ini_set('display_errors', 0);

// Lokasi file token.txt di server lokal
$tokenFile = "token.txt";

// Periksa apakah file token.txt ada dan dapat dibaca
if (!file_exists($tokenFile) || !is_readable($tokenFile)) {
    create_new_token();
    exit;
}

// Ambil token dari file token.txt
$accessToken = trim(file_get_contents($tokenFile));

// Periksa apakah token berhasil diambil
if (empty($accessToken)) {
    create_new_token();
    exit;
}

// URL Debug Token Facebook
$debugUrl = "https://graph.facebook.com/debug_token?input_token={$accessToken}&access_token={$accessToken}";

// Inisialisasi cURL
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $debugUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Eksekusi cURL
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Decode hasil JSON
$data = json_decode($response, true);

// Cek apakah request berhasil atau tidak
if ($httpCode == 200 && isset($data['data']) && $data['data']['is_valid']) {
    echo $accessToken . ""; // Hanya menampilkan token
} else {
    create_new_token();
}

// Fungsi untuk membuat token baru
function create_new_token() {
    function sign_creator(&$data_login) {
        $sig = '';
        foreach ($data_login as $key => $value) {
            $sig .= "$key=$value";
        }
        $sig .= 'c1e620fa708a1d5696fb991c1bde5662';
        $data_login['sig'] = md5($sig);
        return $data_login['sig'];
    }

    function curl_request($url, $post_data, $cookie = null) {
        $useragent = '[FBAN/FB4A;FBAV/417.0.0.33.65;FBBV/480086274;FBDM/{density=1.5,width=720,height=1244};FBLC/en_US;FBRV/0;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N976N;FBSV/7.1.2;FBOP/1;FBCA/x86:armeabi-v7a;]';

        $curl = curl_init();
        $headers = [
            "Connection: keep-alive",
            "Keep-Alive: 300",
            "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7",
            "Accept-Language: en-us,en;q=0.5"
        ];

        curl_setopt_array($curl, [
            CURLOPT_URL => $url,
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => http_build_query($post_data),
            CURLOPT_USERAGENT => $useragent,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_ENCODING => 'gzip, deflate',
            CURLOPT_CONNECTTIMEOUT => 10,
        ]);

        if ($cookie) {
            curl_setopt($curl, CURLOPT_COOKIE, $cookie);
        }

        $response = curl_exec($curl);
        if (curl_errno($curl)) {
            $error = curl_error($curl);
            curl_close($curl);
            return ['error' => true, 'message' => $error];
        }

        curl_close($curl);
        return ['error' => false, 'data' => $response];
    }

    // Token sementara untuk login
    $access_tokens = [
        '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    ];

    // Data login
    $username = 'jayadi002';
    $password = 'cipedangk1234';

    // Generate session ID
    $md5Time = md5(time());
    $hash = sprintf(
        '%s-%s-%s-%s-%s',
        substr($md5Time, 0, 8),
        substr($md5Time, 8, 4),
        substr($md5Time, 12, 4),
        substr($md5Time, 16, 4),
        substr($md5Time, 20, 12)
    );

    foreach ($access_tokens as $current_token) {
        $data_login = [
            'meta_inf_fbmeta' => 'NO_FILE',
            'adid' => '01bffadf-c4e9-4793-b6a4-5894fff7149d',
            'advertiser_id' => '01bffadf-c4e9-4793-b6a4-5894fff7149d',
            'api_key' => '882a8490361da98702bf97a021ddc14d',
            'credentials_type' => 'password',
            'country_code' => 'ID',
            'client_country_code' => 'ID',
            'currently_logged_in_userid' => 0,
            'email' => $username,
            'family_device_id' => $hash,
            'fb_api_caller_class' => "com.facebook.account.login.protocol.Fb4aAuthHandler",
            'fb_api_req_friendly_name' => 'authenticate',
            'format' => 'json',
            'generate_session_cookies' => 1,
            'jazoest' => 22650,
            'locale' => 'id_ID',
            'machine_id' => 'U72FXWwIWwVIPpmp6OLU0x3L',
            'method' => 'auth.login',
            'password' => $password,
            'session_id' => $hash,
            'reg_instance' => $hash,
            'device_id' => $hash,
            'source' => 'loggin',
            'access_token' => $current_token,
        ];

        sign_creator($data_login);
        $response = curl_request('https://b-api.facebook.com/method/auth.login', $data_login);

        if ($response['error']) {
            echo '❌ Gagal membuat token baru: ' . htmlspecialchars($response['message']) . "\n";
            continue;
        }

        $login = $response['data'];
        $tk2 = explode('"access_token":"', $login);
        if (isset($tk2[1])) {
            $tkn2 = explode('","', $tk2[1]);
            $newToken = $tkn2[0];

            // Simpan token ke file token.txt
            file_put_contents("token.txt", $newToken);
            echo $newToken . "\n"; // Hanya menampilkan token
            return;
        } else {
            echo "❌ Gagal mendapatkan token dari respons API.\n";
        }
    }
}
?>
