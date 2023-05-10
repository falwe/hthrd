from creator import create

anticaptcha = 'a4d26ba7ec33ba9aa810449b42a6d011'
kopeechka = '99355de805609eac0dc5750f49fb18e5'
smsactivate = 'b97683d5f482A06051Ab7fc81bb4d495'

session = create(capthaAPI=anticaptcha,
       emailAPI=kopeechka,
       phoneAPI=smsactivate,
       username="playa")
       
token = session.token
# continue, do whatever you want