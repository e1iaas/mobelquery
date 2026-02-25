
export default function Privacy() {
  return (
    <div className="min-h-screen flex flex-col bg-white">

      <main className="flex-1 max-w-3xl mx-auto px-6 py-12 text-gray-700">

        <h1 className="text-2xl font-bold text-gray-900 mb-2">Privacy Policy</h1>
        <p className="text-xs text-gray-400 mb-10">Last updated: {new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' })}</p>

        {/* 1 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">1. Who we are</h2>
          <p className="text-sm leading-relaxed">
            MobelQuery is a furniture search and comparison website that aggregates product listings from trusted EU-based stores. We are the data controller for the purposes of the General Data Protection Regulation (GDPR). For any privacy-related enquiries, contact us at: <a href="mailto:mobelquery@gmail.com" className="text-green-800 hover:underline">mobelquery@gmail.com</a>.
          </p>
        </section>

        {/* 2 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">2. What data we collect</h2>
          <p className="text-sm leading-relaxed">
            We do not collect or store any personally identifiable information (PII) unless you voluntarily contact us. Our servers may log standard technical data such as IP addresses, browser type, and pages visited. These logs are used solely for security and operational purposes and are not shared with third parties.
          </p>
        </section>

        {/* 3 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">3. Cookies</h2>
          <p className="text-sm leading-relaxed mb-3">
            We do not use first-party cookies for tracking or advertising. However, this site contains affiliate links to third-party EU stores. When you click an affiliate link, the partner store may set their own cookies on your device to track purchases for commission purposes. These cookies are set by the third party and governed by their own privacy policy.
          </p>
          <p className="text-sm leading-relaxed">
            Under the EU ePrivacy Directive and GDPR, you have the right to refuse cookies. You can manage or delete cookies at any time through your browser settings. Please note that refusing third-party cookies will not affect your ability to use MobelQuery.
          </p>
        </section>

        {/* 4 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">4. Affiliate links</h2>
          <p className="text-sm leading-relaxed">
            Some links on this site are affiliate links. This means we may earn a small commission if you make a purchase through them, at no extra cost to you. We only link to reputable EU-based stores. Affiliate relationships do not influence how products are ranked or displayed.
          </p>
        </section>

        {/* 5 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">5. Legal basis for processing</h2>
          <p className="text-sm leading-relaxed">
            Where we process any personal data (such as server logs containing IP addresses), we do so on the basis of our legitimate interests in operating and securing this website, in accordance with Article 6(1)(f) of the GDPR.
          </p>
        </section>

        {/* 6 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">6. Data retention</h2>
          <p className="text-sm leading-relaxed">
            Server logs are retained for a maximum of 30 days and are then automatically deleted. We do not retain any other personal data.
          </p>
        </section>

        {/* 7 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">7. Your rights under GDPR</h2>
          <p className="text-sm leading-relaxed">
            As a data subject under the GDPR, you have the right to access, rectify, or erase your personal data; the right to restrict or object to processing; and the right to data portability. You also have the right to lodge a complaint with your local supervisory authority. To exercise any of these rights, contact us at <a href="mailto:eliastestdev@gmail.com" className="text-green-800 hover:underline">eliastestdev@gmail.com</a>.
          </p>
        </section>

        {/* 8 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">8. Third-party links</h2>
          <p className="text-sm leading-relaxed">
            This site links to external websites operated by third parties. We are not responsible for the content or privacy practices of those sites. We encourage you to review the privacy policy of any site you visit.
          </p>
        </section>

        {/* 9 */}
        <section className="mb-8">
          <h2 className="text-base font-semibold text-gray-900 mb-2">9. Changes to this policy</h2>
          <p className="text-sm leading-relaxed">
            We may update this privacy policy from time to time. Any changes will be posted on this page with an updated date. Continued use of the site after changes constitutes acceptance of the updated policy.
          </p>
        </section>

      </main>
    </div>
  )
}