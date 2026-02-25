import { Link } from "react-router-dom"
export default function Header() {
  return (
    <header className="w-full bg-stone-100 border-b border-stone-200 sticky top-0 z-50">
      <div className="max-w-5xl mx-auto px-6 py-5 flex items-center justify-between">

      
        {/* Left: Icon + Brand */}
        <Link to="/">
        <div className="flex items-center gap-3 no-underline">


          {/* Geometric logo: two offset squares in terracotta */}
          <div className="w-9 h-9 flex-shrink-0 flex items-center justify-center">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <rect x="10" y="10" width="16" height="16" rx="2" fill="#c4622d" opacity="0.35" />
              <rect x="6" y="6" width="16" height="16" rx="2" fill="none" stroke="#c4622d" strokeWidth="2" />
              <rect x="18" y="18" width="4" height="4" rx="1" fill="#c4622d" />
            </svg>
          </div>

          {/* Text */}
          <div>
            <h1 className="text-xl font-bold tracking-tight leading-none">
              <span className="text-stone-800">Mobel</span>
              <span className="text-orange-700">Query</span>
            </h1>
            <p className="text-xs text-stone-400 uppercase tracking-widest mt-1 font-medium">
               from verified stores
            </p>
          </div>
        </div>
          </Link>

      </div>
    </header>
  );
}