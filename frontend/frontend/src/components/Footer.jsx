import { Facebook, Twitter, Instagram } from "lucide-react";

export default function Footer() {
  return (
    <footer className="w-full bg-gray-900 text-gray-300 py-10">
  <div className="w-full max-w-6xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
    <div className="text-center md:text-left">
      <h3 className="text-xl font-semibold text-white mb-1">ForgetNot</h3>
      <p className="text-sm text-gray-400">
        © {new Date().getFullYear()} ForgetNot. All rights reserved.
      </p>
    </div>

    <div className="flex space-x-6">
      <a href="#" className="hover:text-primary transition"><Facebook /></a>
      <a href="#" className="hover:text-primary transition"><Twitter /></a>
      <a href="#" className="hover:text-primary transition"><Instagram /></a>
    </div>
  </div>
</footer>

  );
}
