import "./styles.css";

const balance = 1250;

document.querySelector("#app").innerHTML = `
  <header class="topbar">
    <div class="brand"><span class="brand-icon">ع</span><div><strong>عابِد</strong><small>مستحقات العمل الحر</small></div></div>
    <span class="demo-tag">تصور تجريبي</span>
  </header>

  <main class="screen">
    <section class="welcome">
      <p>أهلاً بك</p>
      <h1>مستحقاتك من العمل الحر</h1>
      <span>رصيدك الدولي بالدولار في مكان واحد</span>
    </section>

    <section class="usd-card" aria-label="رصيد الدولار الافتراضي">
      <div class="card-top"><span>رصيد المستقل بالدولار</span><b>USD</b></div>
      <div class="balance" dir="ltr">$${balance.toLocaleString("en-US",{minimumFractionDigits:2,maximumFractionDigits:2})}</div>
      <span class="virtual-label">رصيد افتراضي للعرض التوضيحي</span>
      <div class="divider"></div>
      <div class="destination"><span class="bank-icon">▥</span><div><strong>الحساب البنكي الأساسي</strong><small>يظل حسابك الحالي كما هو</small></div><span class="chevron">‹</span></div>
      <button class="convert-button" id="convert">تحويل للجنيه المصري وإيداعه في الحساب الأساسي بسعر الصرف الرسمي <span>←</span></button>
      <p class="hint">خدمة مقترحة تتيح للمستقل تحويل مستحقاته الدولية إلى حسابه البنكي.</p>
    </section>

    <section class="idea-note">
      <span class="idea-icon">✦</span>
      <div><strong>إضافة جديدة.. دون تغيير التطبيق الأصلي</strong><p>قسم اختياري يسهّل وصول عائدات العمل الحر إلى الحساب البنكي الأساسي.</p></div>
    </section>

    <footer>
      <strong>تصور مقترح للبنك المركزي المصري</strong>
      <p>هذه واجهة توضيحية للفكرة وليست خدمة مصرفية قائمة أو تطبيق InstaPay الرسمي. الرصيد افتراضي، والزر يعرض محاكاة فقط ولا ينفّذ تحويلاً. يتولى البنك المركزي والجهات المصرفية المختصة دراسة واعتماد الجوانب التنظيمية والتقنية وآلية التنفيذ.</p>
      <small>Abid Gateway · Concept Prototype</small>
    </footer>
  </main>

  <div class="modal" id="modal" hidden>
    <section class="modal-card" role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <button class="close" id="close" aria-label="إغلاق">×</button>
      <div class="modal-icon">✓</div>
      <h2 id="modal-title">معاينة فكرة التحويل</h2>
      <p>في التطبيق الفعلي، يتيح هذا الاختيار تحويل مستحقاتك بالدولار إلى الجنيه المصري وإيداعها في حسابك الأساسي، وفق سعر الصرف الرسمي المعتمد وقت التنفيذ.</p>
      <div class="flow"><span>رصيد افتراضي بالدولار</span><b>←</b><span>الحساب البنكي الأساسي بالجنيه</span></div>
      <small>هذه محاكاة للعرض فقط. لا يوجد تحويل أو إيداع حقيقي في هذه النسخة.</small>
      <button class="modal-ok" id="ok">حسناً</button>
    </section>
  </div>
`;

const modal = document.querySelector("#modal");
const closeModal = () => { modal.hidden = true; };
document.querySelector("#convert").addEventListener("click", () => { modal.hidden = false; document.querySelector("#close").focus(); });
document.querySelector("#close").addEventListener("click", closeModal);
document.querySelector("#ok").addEventListener("click", closeModal);
modal.addEventListener("click", event => { if (event.target === modal) closeModal(); });
document.addEventListener("keydown", event => { if (event.key === "Escape" && !modal.hidden) closeModal(); });
