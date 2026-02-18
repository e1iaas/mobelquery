
export default function Terms() {
  return (
    <div className="min-h-screen flex flex-col bg-white">
  

      <main className="flex-1 max-w-3xl mx-auto px-6 py-12 text-gray-700">

        <h1 className="text-2xl font-bold text-gray-900 mb-2">Terms of Use & Affiliate Disclosure</h1>
        <p className="text-xs text-gray-400 mb-10">Last updated: {new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' })}</p>

        {/* 1 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">1. About FurniQuery</h2>
          <p className="text-sm leading-relaxed">
            FurniQuery is a furniture search and comparison website. We aggregate product listings from trusted EU-based third-party retailers. We do not sell, ship, or handle any products directly. All purchases are made through the respective retailer's website.
          </p>
        </section>

        {/* 2 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">2. Accuracy of information</h2>
          <p className="text-sm leading-relaxed">
            Prices, availability, product descriptions, and shipping conditions displayed on FurniQuery are provided by third-party retailers and may change at any time without notice. We make every effort to keep listings up to date, but we cannot guarantee the accuracy or completeness of any product information. Always verify current details on the retailer's website before making a purchase.
          </p>
        </section>

        {/* 3 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">3. Affiliate disclosure</h2>
          <p className="text-sm leading-relaxed">
            Some links on FurniQuery are affiliate links. This means we may earn a small commission from the retailer if you make a purchase after clicking a link, at no additional cost to you. Affiliate relationships do not influence which products are shown, how they are ranked, or the price you pay. We only link to reputable EU-based stores.
          </p>
          <p className="text-sm leading-relaxed mt-3">
            When you click an affiliate link, the partner retailer may set cookies on your device to track the referral. These cookies are governed by the retailer's own privacy and cookie policy. For more information on how we handle data, see our <a href="/privacy" className="text-green-800 hover:underline">Privacy Policy</a>.
          </p>
        </section>

        {/* 4 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">4. Limitation of liability</h2>
          <p className="text-sm leading-relaxed">
            FurniQuery is provided on an "as is" basis. We do not accept liability for any loss or damage arising from your use of this site or any third-party website linked from it, including but not limited to inaccurate product information, failed transactions, or delivery issues. Your contract for any purchase is solely with the retailer, not with FurniQuery.
          </p>
        </section>

        {/* 5 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">5. Consumer rights</h2>
          <p className="text-sm leading-relaxed">
            Nothing in these terms affects your statutory rights as a consumer under EU law, including your rights under the EU Consumer Rights Directive and applicable national consumer protection legislation. For any issues with a product or purchase, contact the retailer directly.
          </p>
        </section>

        {/* 6 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">6. Intellectual property</h2>
          <p className="text-sm leading-relaxed">
            Product images and descriptions displayed on FurniQuery are the property of the respective retailers and are used for comparison purposes. The FurniQuery name, logo, and original site content are our intellectual property and may not be reproduced without permission.
          </p>
        </section>

        {/* 7 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">7. Changes to these terms</h2>
          <p className="text-sm leading-relaxed">
            We may update these terms from time to time. Any changes will be posted on this page with an updated date. Continued use of the site after changes are posted constitutes your acceptance of the updated terms.
          </p>
        </section>

        {/* 8 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">8. Contact</h2>
          <p className="text-sm leading-relaxed">
            For any questions about these terms, contact us at: <a href="mailto:eliastestdev@gmail.com" className="text-green-800 hover:underline">eliastestdev@gmail.com</a>
          </p>
        </section>

      </main>

     
    </div>
  )
}