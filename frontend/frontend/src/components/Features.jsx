export default function Features() {
  const features = [
    { title: "Voice Journaling", desc: "Record with one tap, no typing." },
    { title: "Smart Summaries", desc: "AI turns rambles into clear notes." },
    { title: "Gentle Reminders", desc: "Soft nudges with calming quotes." },
  ];

  return (
    <section
  id="features"
  className="w-full min-h-screen flex items-center justify-center bg-white px-6"
>
  <div className="w-full max-w-6xl text-center">
    <h2 className="text-3xl font-bold mb-12 text-primary">Why ForgetNot?</h2>

    <div className="grid md:grid-cols-3 gap-10">
      {features.map((f) => (
        <div
          key={f.title}
          className="p-6 rounded-2xl shadow hover:shadow-lg transition-shadow"
        >
          <h3 className="text-xl font-semibold mb-3">{f.title}</h3>
          <p className="text-gray-600">{f.desc}</p>
        </div>
      ))}
    </div>
  </div>
</section>

  );
}
