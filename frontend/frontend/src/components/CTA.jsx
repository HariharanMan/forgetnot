import { motion } from "framer-motion";

export default function CTA() {
  return (
    <section
  className="w-full min-h-screen flex items-center justify-center bg-primary text-white text-center"
>
  <motion.div
    initial={{ opacity: 0, scale: 0.95 }}
    whileInView={{ opacity: 1, scale: 1 }}
    transition={{ duration: 0.6 }}
    viewport={{ once: true }}
    className="max-w-3xl px-6"
  >
    <h2 className="text-3xl md:text-4xl font-extrabold mb-4">
      Ready to Clear Your Mind?
    </h2>
    <p className="text-lg md:text-xl mb-10 text-blue-800">
      Start speaking freely and let ForgetNot handle the rest—your gentle
      companion for a clutter-free mind.
    </p>
    <a
      href="#"
      className="inline-block px-8 py-3 bg-white text-primary rounded-full font-medium shadow-lg hover:shadow-xl transition"
    >
      Join the Waitlist
    </a>
  </motion.div>
</section>

  );
}
