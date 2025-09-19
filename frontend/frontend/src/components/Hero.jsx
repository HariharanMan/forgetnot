import { motion } from "framer-motion";

export default function Hero() {
  return (
    <section
  className="relative flex flex-col items-center justify-center min-h-screen w-full text-center bg-gradient-to-b from-indigo-50 to-white px-6"
>
  <motion.h1
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.8 }}
    className="text-5xl md:text-6xl font-extrabold text-primary mb-4"
  >
    ForgetNot
  </motion.h1>

  <p className="max-w-xl text-lg md:text-xl text-gray-600 mb-8">
    Speak your thoughts. Breathe easy. Let our mindful voice-based
    journaling & reminders clear your mind.
  </p>

  <motion.a
    href="#services"
    whileHover={{ scale: 1.05 }}
    className="px-8 py-3 bg-primary text-white rounded-full font-medium shadow-lg hover:shadow-xl transition"
  >
    Get Started
  </motion.a>
</section>


  );
}
