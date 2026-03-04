const steps = [
  {
    number: "1",
    heading: "Describe it naturally",
    text: "Type what you're looking for in plain language — no filters, no categories.",
  },
  {
    number: "2",
    heading: "We finds the closest matches",
    text: "Our semantic search understands meaning, not just keywords, across verified EU stores.",
  },
  {
    number: "3",
    heading: "Buy directly from the store",
    text: "Click through to the retailer and purchase with full EU consumer protection.",
  },
]

export default function HowItWorks() {
  return (
    <div className="max-w-4xl mx-auto px-6 py-16">
      <p className="text-xs text-orange-700 uppercase tracking-widest font-semibold text-center mb-10">
        How it works
      </p>
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-8">
        {steps.map((step) => (
          <div key={step.number} className="text-center">
            <div className="w-12 h-12 bg-orange-50 rounded-2xl flex items-center justify-center mx-auto mb-4">
              <span className="text-lg font-bold text-orange-700">{step.number}</span>
            </div>
            <h3 className="font-bold text-stone-800 mb-2">{step.heading}</h3>
            <p className="text-stone-500 text-sm leading-relaxed">{step.text}</p>
          </div>
        ))}
      </div>
    </div>
  )
}