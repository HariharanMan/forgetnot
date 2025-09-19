import { motion } from "framer-motion";
import { Mic, Sparkles, Bell } from "lucide-react";

export default function Services() {
  const services = [
    {
      icon: <Mic className="w-10 h-10 text-primary" />,
      title: "Effortless Voice Capture",
      desc: "Just tap and speak. ForgetNot instantly records your thoughts without friction."
    },
    {
      icon: <Sparkles className="w-10 h-10 text-primary" />,
      title: "AI-Powered Summaries",
      desc: "Our AI distills long rambles into clear, concise notes and journals."
    },
    {
      icon: <Bell className="w-10 h-10 text-primary" />,
      title: "Gentle Reminders",
      desc: "Receive soft, quote-based nudges to stay organized and uplifted."
    }
  ];

  return (
    <section
  id="services"
  className="w-full min-h-screen flex items-center justify-center bg-gradient-to-b from-white to-indigo-50 px-6"
>
  <div className="w-full max-w-6xl text-center">
    <motion.h2
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      viewport={{ once: true }}
      className="text-3xl md:text-4xl font-bold text-primary mb-12"
    >
      What ForgetNot Offers
    </motion.h2>

    <div className="grid md:grid-cols-3 gap-10">
      {services.map((s, i) => (
        <motion.div
          key={s.title}
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: i * 0.1 }}
          viewport={{ once: true }}
          className="p-8 rounded-2xl shadow-md bg-white hover:shadow-xl transition"
        >
          <div className="flex justify-center mb-4">{s.icon}</div>
          <h3 className="text-xl font-semibold mb-2">{s.title}</h3>
          <p className="text-gray-600">{s.desc}</p>
        </motion.div>
      ))}
    </div>
  </div>
</section>

  );
}
