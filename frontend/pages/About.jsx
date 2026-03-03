import { Link } from "react-router-dom"

export default function About() {
  return (
    <main className="flex-1 w-full">
      <div className="max-w-3xl mx-auto px-6 pt-16 pb-20">

        {/* Header */}
        <div className="mb-12">
          <p className="text-xs text-orange-700 uppercase tracking-widest font-semibold mb-3">About</p>
          <h1 className="text-4xl font-bold text-gray-900 tracking-tight leading-tight">
            Search furniture the way<br />
            <span className="text-orange-700">you think about it</span>
          </h1>
        </div>

        {/* What is MobelQuery */}
        <section className="mb-10">
          <h2 className="text-lg font-bold text-stone-800 mb-3">What is MobelQuery?</h2>
          <p className="text-stone-600 leading-relaxed">
            MobelQuery is an AI-powered furniture search engine built for the Nordic market.
            Instead of filtering through endless dropdowns and categories, you simply describe
            what you're looking for — in plain language — and our semantic search engine finds
            the closest matches across verified EU furniture stores.
          </p>
          <p className="text-stone-600 leading-relaxed mt-4">
            Try searching for <span className="text-orange-700 font-medium">"cozy sofa for a small living room"</span> or{" "}
            <span className="text-orange-700 font-medium">"minimalist oak dining table"</span> and see the difference
            compared to traditional keyword search.
          </p>
        </section>

        {/* Why we built it */}
        <section className="mb-10">
          <h2 className="text-lg font-bold text-stone-800 mb-3">Why we built it</h2>
          <p className="text-stone-600 leading-relaxed">
            Finding furniture online is frustrating. Most search engines are built for exact keywords,
            not human thought. You know what feeling you want — warm, Scandinavian, compact, industrial —
            but translating that into a keyword search rarely works.
          </p>
          <p className="text-stone-600 leading-relaxed mt-4">
            We built MobelQuery to fix that. Using modern semantic AI models, we match the meaning
            behind your words to the right products — not just the literal text.
          </p>
        </section>

        {/* Who we are */}
        <section className="mb-10">
          <h2 className="text-lg font-bold text-stone-800 mb-3">Who we are</h2>
          <p className="text-stone-600 leading-relaxed">
            MobelQuery is an independent project built in Sweden. We're focused on making
            furniture discovery smarter and more human — starting with the Nordic market and expanding
            from there.
          </p>
        </section>

        {/* Contact */}
        <section className="mb-12">
          <h2 className="text-lg font-bold text-stone-800 mb-3">Contact</h2>
          <p className="text-stone-600 leading-relaxed">
            Questions, feedback, or partnership inquiries? We'd love to hear from you.
          </p>
          <a
            href="mailto:mobelquery@gmail.com"
            className="inline-block mt-3 text-orange-700 font-semibold hover:underline"
          >
            mobelquery@gmail.com
          </a>
        </section>

        {/* CTA */}
        <div className="border-t border-stone-200 pt-10 text-center">
          <p className="text-stone-500 mb-4 text-sm">Ready to find your next piece of furniture?</p>
          <Link
            to="/"
            className="inline-block bg-orange-700 text-white text-sm font-semibold px-6 py-3 rounded-xl hover:bg-orange-600 transition-colors"
          >
            Start searching →
          </Link>
        </div>

      </div>
    </main>
  )
}