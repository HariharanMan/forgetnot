import { motion } from "framer-motion";
import Hero from "./components/Hero";
import Features from "./components/Features";
import Services from "./components/Services";
import CTA from "./components/CTA";
import Footer from "./components/Footer";
import './App.css';

export default function App() {
  return (
    <div className="w-full bg-gradient-to-b from-indigo-50 to-white text-gray-900 py-20">
      <Hero />
      <Features />
      <Services />
      <CTA />
      <Footer />
    </div>
  );
}
