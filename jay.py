def clear():
    os.system('clear')
#_____________________[ANIMATION BOX]____________________________#
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.1)
def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first,last
def extractor(data):
    try:
        soup = BeautifulSoup(data,"html.parser")
        data = {}
        for inputs in soup.find_all("input"):
            name = inputs.get("name")
            value = inputs.get("value")
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {"error":str(e)}
def GetEmail():
    try:
        response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
        return response['email']
    except:
        return None
def GetCode(email):
    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
        code = re.search(r'FB-(\d+)', response).group(1)
        return code
    except:
        return None
def banner():
    os.system("clear")
    print(f"{W}┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑")
    print(f"{W}│ {R}►{G} ONWER {R}:{G} 𝐌𝐎𝐍𝐗𝐓𝐄𝐑 𝐈𝐍𝐒𝐈𝐈𝐃𝐄         {W}│")
    print(f"{W}│ {R}►{G} TOOL  {R}:{G} 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐀𝐔𝐓𝐎 𝐂𝐑𝐄𝐀𝐓𝐄 {W}│")
    print(f"{W}│ {R}►{G} TYPE  {R}:{G} 𝐏𝐑𝐄𝐌𝐈𝐔𝐌            {W}  │")
    print(f"{W}┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")
def linex():
    print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def main() -> None:
    banner()
    input(f"  {R}►{G} PRESS YOUR ENTER BUTTON\x1b[38;5;196m.\x1b[38;5;46m.\x1b[1;97m.\033[1;34m. ")
    linex()
    for make in range(100):
        ses = requests.Session()
        response = ses.get(
            url='https://touch.facebook.com/reg',
            params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},
        )
        formula = extractor(response.text)
        email2 = GetEmail()
        firstname,lastname = fake_name()
        print(f"  {R}►{G} ACCOUNT CREATE STARTED")
        animation(f"  {R}►{G} ACCOUNT NAME  {R}:{G} {firstname} {lastname}")
        animation(f"  {R}►{G} ACCOUNT EMAIL {R}:{G} {email2}");linex()
        animation(f"  {R}►{G} WAITING SOME TIME\x1b[38;5;196m.\x1b[38;5;46m.\x1b[1;97m.\033[1;34m.")
        payload = {
            'ccp': "2",
            'reg_instance': str(formula["reg_instance"]),
            'submission_request': "true",
            'helper': "",
            'reg_impression_id': str(formula["reg_impression_id"]),
            'ns': "1",
            'zero_header_af_client': "",
            'app_id': "103",
            'logger_id': str(formula["logger_id"]),
            'field_names[0]': "firstname",
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': "birthday_wrapper",
            'birthday_day': str(random.randint(1,28)),
            'birthday_month': str(random.randint(1,12)),
            'birthday_year': str(random.randint(1992,2009)),
            'age_step_input': "",
            'did_use_age': "false",
            'field_names[2]': "reg_email__",
            'reg_email__': email2,
            'field_names[3]': "sex",
            'sex': "2",
            'preferred_pronoun': "",
            'custom_gender': "",
            'field_names[4]': "reg_passwd__",
            'name_suggest_elig': "false",
            'was_shown_name_suggestions': "false",
            'did_use_suggested_name': "false",
            'use_custom_gender': "false",
            'guid': "",
            'pre_form_step': "",
            'encpass': f"#PWD_BROWSER:{str(time.time())[:10]}:MONI@1234@",
            'submit': "Sign Up",
            'fb_dtsg': "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",
            'jazoest': str(formula["jazoest"]),
            'lsd': str(formula["lsd"]),
            '__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",
            '__csr': "",
            '__req': "p",
            '__fmt': "1",
            '__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",
            '__user': "0"
        }
        header1 = {
            "Host":"m.facebook.com",
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.135 Mobile Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "dnt":"1",
            "X-Requested-With":"mark.via.gp",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "dpr":"1.75",
            "viewport-width":"980",
            "sec-ch-ua":"\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
            "sec-ch-ua-mobile":"?1",
            "sec-ch-ua-platform":"\"Android\"",
            "sec-ch-ua-platform-version":"\"\"",
            "sec-ch-ua-model":"\"\"",
            "sec-ch-ua-full-version-list":"",
            "sec-ch-prefers-color-scheme":"dark",
            "Accept-Encoding":"gzip, deflate, br, zstd",
            "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
        }
        reg_url = "https://m.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1"
        py_submit = ses.post(reg_url, data=payload, headers=header1)
        if "c_user" in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok["c_user"])
            header2 = {
                'authority': 'm.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'dpr': '2',
                'referer': 'https://m.facebook.com/login/save-device/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.135 Mobile Safari/537.36',
                'viewport-width': '980',      
            }
            params = {
                'next': 'https://m.facebook.com/?deoia=1',
                'soft': 'hjk',
            }
            con_sub = ses.get('https://x.facebook.com/confirmemail.php', params=params, headers=header2).text
            valid = GetCode(email2)
            if valid:
                cookie = (";").join([ "%s=%s" % (key,value) for key,value in ses.cookies.get_dict().items()])
                animation(f"  {R}►{G} ACCOUNT OTP {R}:{G} {valid}")
                animation(f"  {R}►{G} ACCOUNT UID {R}:{G} {uid}")
                animation(f"  {R}►{G} ACCOUNT PASSWORD {R}:{G} MONI@1234@")
                print(f"  {R}►{G} COOKIES {R}: {W}{cookie}")
                open("/sdcard/OK.txt","a").write(uid+"|MONI@1234@|"+valid+"|"+cookie+"|"+email2+"\n")
                linex()
            else:
                print(f"{R}Account Checkpoint Successfully!")
                linex()
main()
