import "./styles.css";

const money = (n, currency) => new Intl.NumberFormat("en-US", {style:"currency",currency,minimumFractionDigits:2,maximumFractionDigits:2}).format(n);
const rate = 49.8, balance = 1250;
const rows = [
  ["دفعة تصميم واجهة","04 نوفمبر 2026","AB-DEMO-1042",420],
  ["مهمة تطوير برمجيات","01 نوفمبر 2026","AB-DEMO-1038",680],
  ["استشارة تقنية","28 أكتوبر 2026","AB-DEMO-1029",150]
];
const transactions = rows.map(t => '<article class="transaction-row"><span class="transaction-icon">↙</span><div class="transaction-info"><strong>'+t[0]+'</strong><span>'+t[1]+' · '+t[2]+'</span><small>تم الاستلام — محاكاة فقط</small></div><b class="transaction-amount" dir="ltr">'+money(t[3],"USD")+'</b></article>').join("");

document.querySelector("#app").innerHTML =
'<header class="topbar"><div class="identity"><div class="brand-mark">ع</div><div class="identity-copy"><strong>عابِد</strong><span>بوابة العمل الحر الدولي</span></div></div><div class="profile"><span class="demo-pill"><i></i> وضع تجريبي</span><span class="avatar">ع</span></div></header>'+
'<main class="app-main" id="home"><section class="greeting"><div><p class="eyebrow">مرحباً بعودتك</p><h1>علي حسين فكري</h1><p class="greeting-sub">إليك ملخص حسابك وحركة مستحقات العمل الحر.</p></div><div class="greeting-icon">✦</div></section>'+
'<section class="bank-card panel"><div class="card-topline"><span class="card-kicker">الحساب البنكي الأساسي</span><span class="bank-symbol">▥</span></div><h2>البنك الأهلي المصري</h2><p class="bank-type">حساب توفير · مرجع تجريبي</p><div class="account-number"><span>معرّف الحساب</span><b dir="ltr">NBE-DEMO-2048</b></div></section>'+
'<section class="usd-card"><div class="usd-heading"><div><span class="card-kicker">حساب العمل الحر الدولي</span><h2>رصيد الدولار الأمريكي</h2></div><span class="currency-badge">USD</span></div><p class="balance-label">الرصيد التجريبي المتاح</p><div class="balance" dir="ltr">$1,250.00</div><div class="iban-box"><span>Virtual IBAN · مرجع افتراضي فقط</span><strong dir="ltr">ABID •••• •••• 2048</strong></div><button class="primary-action" id="settle">تحويل تقديري إلى الجنيه المصري <span>←</span></button><p class="rate-note">حساب توضيحي على سعر افتراضي '+rate.toFixed(2)+' جنيه لكل دولار — ليس سعر صرف فعلياً.</p></section>'+
'<section class="quick-section"><div class="section-heading"><div><p class="eyebrow">اختصاراتك</p><h2>الخدمات السريعة</h2></div></div><div class="quick-grid"><button class="quick-tile" id="receive"><span class="quick-icon">⇩</span><strong>بيانات الاستقبال</strong><small>عرض المرجع التجريبي</small></button><button class="quick-tile" id="transfer"><span class="quick-icon">⇄</span><strong>التحويلات</strong><small>مراجعة سجل المحاكاة</small></button><button class="quick-tile" id="settings"><span class="quick-icon">⚙</span><strong>الإعدادات</strong><small>معلومات النموذج</small></button></div></section>'+
'<section class="transactions-section" id="transactions"><div class="section-heading"><div><p class="eyebrow">حركة الحساب</p><h2>آخر المعاملات</h2></div><span class="records-count">3 سجلات تجريبية</span></div><div class="transactions-list">'+transactions+'</div><div class="summary-card"><span>إجمالي الرصيد التوضيحي بالجنيه</span><strong dir="ltr">'+money(balance*rate,"EGP")+'</strong></div></section>'+
'<footer class="disclaimer"><strong>تنويه مهم — نموذج تجريبي</strong><p>هذه واجهة تصورية لأغراض العرض والبحث فقط. الحساب البنكي ومرجع الدولار والرصيد وسعر الصرف والمعاملات بيانات افتراضية. لا يوجد IBAN حقيقي أو ربط مع البنك الأهلي أو InstaPay، ولا تنفّذ الصفحة أي تحويلات مالية. لا تُدخل بياناتك البنكية الحقيقية.</p><span>Abid Gateway · Prototype 0.1.0</span></footer></main>'+
'<nav class="bottom-nav" aria-label="التنقل الرئيسي"><button class="nav-item active" id="nav-home" aria-current="page"><span>⌂</span><small>الرئيسية</small></button><button class="nav-item" id="nav-transfers"><span>⇄</span><small>التحويلات</small></button><button class="nav-item" id="nav-settings"><span>⚙</span><small>الإعدادات</small></button></nav>'+
'<div class="dialog-backdrop" id="dialog" hidden><section class="dialog-card" role="dialog" aria-modal="true" aria-labelledby="dialog-title"><button class="dialog-close" id="close" aria-label="إغلاق">×</button><p class="eyebrow">محاكاة آمنة</p><h2 id="dialog-title"></h2><p id="dialog-copy"></p><aside id="dialog-detail"></aside><button class="primary-action" id="ok">حسناً، فهمت</button></section></div>';

const dialog = document.querySelector("#dialog");
const showDialog = (title, copy, detail) => {
  document.querySelector("#dialog-title").textContent=title;
  document.querySelector("#dialog-copy").textContent=copy;
  document.querySelector("#dialog-detail").textContent=detail;
  dialog.hidden=false; document.querySelector("#close").focus();
};
const closeDialog=()=>{dialog.hidden=true;};
document.querySelector("#receive").addEventListener("click",()=>showDialog("بيانات استقبال افتراضية","لا يصدر حساب الاستقبال الفعلي إلا عن بنك أو مقدم خدمات مالية مرخص وبعد إجراءات التحقق.","Demo Reference: ABID-USD-2048 — ليس IBAN أو حساباً حقيقياً."));
document.querySelector("#settle").addEventListener("click",()=>showDialog("تسوية تقديرية بالجنيه","هذه عملية حسابية توضيحية فقط وليست سعر صرف أو أمراً بتحويل الأموال.",money(balance,"USD")+" × "+rate.toFixed(2)+" = "+money(balance*rate,"EGP")+" — سعر افتراضي."));
const goToTransactions=()=>document.querySelector("#transactions").scrollIntoView({behavior:"smooth",block:"start"});
document.querySelector("#transfer").addEventListener("click",goToTransactions);
document.querySelector("#nav-transfers").addEventListener("click",goToTransactions);
document.querySelector("#settings").addEventListener("click",()=>showDialog("إعدادات النموذج","هذه نسخة عرض تجريبية ولا تحفظ بيانات شخصية أو مالية ولا تتصل بأي مؤسسة مالية.","Abid Gateway · Prototype 0.1.0"));
document.querySelector("#nav-settings").addEventListener("click",()=>document.querySelector("#settings").click());
document.querySelector("#nav-home").addEventListener("click",()=>window.scrollTo({top:0,behavior:"smooth"}));
document.querySelector("#close").addEventListener("click",closeDialog);
document.querySelector("#ok").addEventListener("click",closeDialog);
dialog.addEventListener("click",e=>{if(e.target===dialog)closeDialog();});
document.addEventListener("keydown",e=>{if(e.key==="Escape"&&!dialog.hidden)closeDialog();});
