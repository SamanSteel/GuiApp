# Standard Library
from typing import Dict

# Third Library
from pydantic_settings import BaseSettings, SettingsConfigDict


class Page(BaseSettings):
    model_config = SettingsConfigDict()
    PAGE_DICT: Dict = {
        "صفحه اصلی": "",
        "انبار": {"جستجو کالا و مرکز هزینه": "http://192.168.20.19/"},
        "رافا": {
            "شیرپوینت": "http://home.rafa-group.com/sites/FSY/SitePages/%D8%AE%D8%A7%D9%86%D9%87.aspx",
            "نرم افزار پارسه": "http://rafa-net.rafa-group.com/",
        },
        "باسکول": {
            "مشاهده اطلاعات": "http://192.168.20.3/default.aspx",
            "اصلاح قبض": "http://192.168.20.3/editfrm.aspx",
            "درخواستهای اصلاح قبض": "http://192.168.20.3/EditReqFrm.aspx",
        },
        "اسناد و مدارک":{
            "بایگانی نت":""
        },
        "صورتجلسات":{
            "ثبت صورتجلسه":"",
            "پیگیری صورتجلسه":"",
            "لیست صورتجلسات":"",
        },
        "هاپر": {
            "موجودی لحظه‌ای هاپر": "http://192.168.20.3/HooperInvPageD.aspx",
            "مصرف اسفنجی": "http://192.168.20.3/SpongeHandlingPage.aspx",
            "گردش هاپر": "http://192.168.20.3/HooperInvHandlingPage.aspx",
            "اصلاح رکورد": "http://192.168.20.3/HooperInvEditPage.aspx",
        },
        "دیسپاچینگ": {
            "دیسپاچینگ": "http://192.168.20.3/pages/dispatchrpt.aspx",
            "گراف دیسپاچینگ": "http://192.168.20.3/dispatchgraph.aspx",
        },
        "سیستم انرژی": {
            "انرژی لحظه‌ای": "http://192.168.20.3/PowerGraphOnline.aspx",
            "انرژی مصرفی": "http://192.168.20.3/PowerGraphReport.aspx",
            "توقفات سیستم انرژی": "http://192.168.20.3/pages/EnergyStops.aspx",
        },
        "سناریو": {
            "ثبت موجودی": "http://192.168.20.3/pages/InvReg.aspx",
            "ثبت سناریو و برنامه": "http://192.168.20.3/pages/NewSenario.aspx",
            "مغایرت سناریو": "http://192.168.20.3/pages/NCSenario.aspx",
            "بار تحویل شده": "http://192.168.20.3/pages/PrdDeliverPg.aspx",
        },
        "تولید": {
            "ثبت اطلاعات ذوب": "http://192.168.20.3/RegMeltinfo2.aspx",
            "لیست اطلاعات ذوب": "http://192.168.20.3/pages/PrdReport.aspx",
            "ثبت توقفعات": "http://192.168.20.3/RegStpp4.aspx",
            "لیست توقفات": "http://192.168.20.3/StoppsReport.aspx",
            "توقفات بررسی نشده": "http://192.168.20.3/nonregstp4.aspx",
            "آماده سازی پاتیل": "http://192.168.20.3/pages/PrPatilPage.aspx",
            "نسوزکاری پاتیل": "http://192.168.20.3/pages/PatilFireProofTbl.aspx",
            "ریخته‌گری پاتیل": "http://192.168.20.3/pages/PatilCastingPg.aspx",
            "آماده سازی تاندیش": "http://192.168.20.3/pages/prTandishPg.aspx",
            "نسوزکاری تاندیش": "http://192.168.20.3/pages/TandishFireProof.aspx",
            "نسوزکاری کوره": "http://192.168.20.3/pages/FRFireProofTbl.aspx",
            "سکوئنس": "http://192.168.20.3/pages/SequencePg.aspx",
            "کوتینگ": "http://192.168.20.3/pages/CoatingPage.aspx",
            "درخواست چنج بوته": "http://192.168.20.3/pages/ChangeButePg.aspx",
        },
        "سامانه جامع گزارشات":"192.168.1.18",
        "کنترل کیفیت": {"لیست آنالیز ذوب": "http://192.168.20.3:800/pages/QCReport.aspx"},
        "مدیریت نرم افزار": "",
    }


page_settings = Page()
