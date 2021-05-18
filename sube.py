texto='''E-112 493ET5,8887620,,,
E-153 897ET7,864352044068542,,,
E-158 72AJ8C,8516612,,,
E-210 914AL4,8893030,,,
E-100 64AG1T,580014270,,,
E-101 45AK1D,866856039975451,,,
E-102 73AB8Y,580001510,,,
E-103 231EY4 ,864352044595072,,,
E-104 248EX2 ,864352044593440,,,
E-107 09AK2R,8784971,,,
E-108 95AJ9S,864352044594695,,,
E-109 46AK1D,8863095,,,
E-110 63AJ7Z,8748745,,,
E-111 89AE4D,8742665,,,
E-113 035EV5,8863378,,,
E-114 36AK2L ,580011599,,,
E-115 93AS5A,8893851,,,
E-116 17AG3X,8893837,,,
E-117 94AS5A,8792890,,,
E-118 062EV5 ,864606049713547,,,
E-119 65AG1T,107889862,,,
E-120 8508479,8792417,,,
E-121 16AG3X ,864606048145055,,,
E-122 86AN1F,8782801,,,
E-123 31AK5S,10187577,,,
E-124 93AG4T,8863729,,,
E-126 789AS4	,8883189,,,
E-126P 92AG4T,864352044594026,,,
E-127 70AG2C,8893781,,,
E-128 057EV5,8882194,,,
E-129 655EY9,864292042907764,,,
E-130 494AK9,8893990,,,
E-130P 80AJ7C,864352044593119,,,
E-131 654EY9 ,864352044066975,,,
E-132 32AK5S,580017265,,,
E-133 91AG4T,8893842,,,
E-135 71AJ9S,580001489,,,
E-136 011EZ1,8508471,,,
E-138 33AK5S,580011603,,,
E-139 729DN7 ,864352044062909,,,
E-140 18AG3X,8863766,,,
E-142 92AS5A ,864352044595098,,,
E-143 426DN1,8877062,,,
E-144 91AED ,864352044594265,,,
E-145 92AK3L,10180280,,,
E-146 91AK3L,8893839,,,
E-148 295AM8 ,864352044065829,,,
E-150 LA46510,580004024,,,
E-151 310DP2 ,864352044591139,,,
E-154 28AB8X,868998030912816,,,
E-155 02AE8H,8863100,,,
E-156 061EV5 ,864352044594745,,,
E-157 15AG3X,864352044590826,,,
E-160 LA84787,8889929,,,
E-161 69AB31,864352044591378,,,
E-163 37AE9C,8782921,,,
E-164 79AB8W,8872729,,,
E-166 84AN1F,8863456,,,
E-167 27ABBX,580017266,,,
E-168 50AH4G ,864352044590768,,,
E-169 26AF5N,8511085,,,
E-170 24AF5N,8865428,,,
E-172 55AG6N,8866581,,,
E-174 54AG6N,8889922,,,
E-175 57AG6N,864352044932788,,,
E-176 58AG6N,8893845,,,
E-177 95AG8W,8863762,,,
E-178 24AH1W,8508479,,,
E-181 LA67425 ,864352044590834,,,
E-185 31AK2U,8890068,,,
E-187 91AK1U,8719174,,,
E-189 05AL4C,864507031313512,,,
E-190 29AA5C,8866950,,,
E-191 61AL5T,8866979,,,
E-194 93AN2F,8792482,,,
E-196 49AN5F,8893848,,,
E-197 66AN1J,864507038430087,,,
E-199 62AN9Y,8893448,,,
E-200 60AP7Z,10056793,,,
E-201 63AP67,8718348,,,
E-203 62AP6Z,864352044591329,,,
E-204 60AP6Z,580010557,,,
E-206 64AP6Z-Corralon,864606049715955,,,
E-207 39AS4A,864352044066884,,,
E-208 315DF7,8893840,,,
E-209 19AE8B,864352044593556,,,
E-211 097AM3 ,864352044593382,,,
E-301 956AN4,580008975,,,
E-302 573AL7,8511075,,,
E-303 859DC7,8718673,,,
E-305 16UF8H,8893841,,,
E-580 sinplacas,8865265,,,
P-322 13AP1P,864352044921765,,,
P-325 14AP1P,864352044590701,,,
R-28 sinplacas,865284041125174,,,
R-214 sinplacas,865284045616111,,,
R-243 sinplacas,8742669,,,
R-250 sinplacas,864352044923340,,,
R-259 10UF8H,8743617,,,
R-284 sinplacas,8061946,,,
R-321 sinplacas,864352044923100,,,'''

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://gpscontrol:qazwsxedc@127.0.0.1/bridge?charset=utf8'
db = SQLAlchemy(app)

class Devices(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    imei = db.Column(db.String(16))
    email = db.Column(db.String(64), index=True)
    sn = db.Column(db.String(16))
    password = db.Column(db.String(16))
    creation_date = db.Column(db.DateTime,default=datetime.utcnow())
    mygroup = db.Column(db.String(40))
    ff0=db.Column(db.Integer)
    log = db.Column(db.Text(), default=u'')
    plates = db.Column(db.String(10))
    protocol=db.Column(db.Integer)
    lastupdate = db.Column(db.DateTime, default=datetime.utcnow())
    eco = db.Column(db.String(30))
    latitude = db.Column(db.Numeric(10, 6))
    longitude = db.Column(db.Numeric(11, 6))
    altitude = db.Column(db.Integer)
    speed = db.Column(db.Float)
    angle = db.Column(db.Float)
    url = db.Column(db.Text())
    vin = db.Column(db.String(40))
    enterprise = db.Column(db.String(50))
    event_code = db.Column(db.String(2))
    telephone = db.Column(db.String(255), default=u'')
    device_key = db.Column(db.String(255), default=u'')
    name = db.Column(db.String(255), default=u'')
    last_alarm = db.Column(db.DateTime)
    alarm_status = db.Column(db.String(25), default=u'')
    last_followme = db.Column(db.DateTime)
    followme_status = db.Column(db.String(25), default=u'')
    last_name = db.Column(db.String(30), default=u'')
    maiden_name = db.Column(db.String(30), default=u'')
    street = db.Column(db.String(255), default=u'')
    delegacion = db.Column(db.String(255), default=u'')
    number = db.Column(db.String(15), default=u'')
    zip = db.Column(db.String(10), default=u'')
    colonia = db.Column(db.String(255), default=u'')
    panic = db.Column(db.String(5), default=u'false')
    dvr = db.Column(db.String(1), default=u'N')
    alarmcount= db.Column(db.Integer,default=0)
    alt_lat = db.Column(db.Numeric(10, 6))
    alt_lon = db.Column(db.Numeric(11, 6))
    tipodeunidad = db.Column(db.String(255), default=u'')
    marca = db.Column(db.String(255), default=u'')
    submarca = db.Column(db.String(255), default=u'')
    fechamodelo = db.Column(db.Integer)
    zona = db.Column(db.String(255), default=u'')
    municipio = db.Column(db.String(255), default=u'')
    numconsesion = db.Column(db.String(255), default=u'')

query = Devices.query.filter_by().all()
for item in query:
    print(item.imei)
l=texto.split("\n")
for item in l:
    fields=item.split(",")
    ecolist=fields[0]
    placalist=ecolist.split(" ")
    eco=placalist[0]
    placas=placalist[1]
    imei=fields[1]
    newimei = Devices(imei=imei,sn=eco,password="1",mygroup="ms03",email="admin",plates=placas,protocol=54,eco=eco,panic=False,dvr="N")
    db.session.add(newimei)
    db.session.commit()
    print(eco,placas, imei)
