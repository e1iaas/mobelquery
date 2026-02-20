export default function Footer() {
  return (
    <footer className="w-full bg-stone-800 border-t border-stone-700 mt-12">
      <div className="max-w-5xl mx-auto px-6 py-8">

        {/* Top row: brand + links */}
        <div className="flex items-center justify-between mb-4">
          <p className="text-stone-100 font-bold text-lg tracking-tight">
            Mobel<span className="text-orange-400">Query</span>
          </p>
          <div className="flex gap-6">
            <a href="/privacy" className="text-stone-400 text-sm font-medium hover:text-orange-400">
              Privacy Policy
            </a>
            <a href="/terms" className="text-stone-400 text-sm font-medium hover:text-orange-400">
              Terms
            </a>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t border-stone-700 mb-4" />

        {/* Bottom row: copyright + disclaimer */}
        <div className="flex flex-col gap-1">
          <p className="text-stone-400 text-sm">
            © {new Date().getFullYear()} MobelQuery
          </p>
          <p className="text-stone-600 text-xs leading-relaxed">
            Some links on this site are affiliate links. We may earn a commission if you purchase through them at no extra cost to you.
          </p>
        </div>

      </div>
    </footer>
  )
}