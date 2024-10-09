from flask import Flask, render_template, request, jsonify
import webbrowser
import time
from threading import Thread

app = Flask(__name__)

# Global variables
domains = []
generated_urls = []

def try_variations(domain):
    domain = domain.strip().lower()
    if domain.startswith('http://') or domain.startswith('https://'):
        domain = domain.split('://', 1)[1]
    variations = [
        domain,
        f"www.{domain}" if not domain.startswith('www.') else domain[4:],
    ]
    return variations

def generate_semrush_urls():
    global generated_urls
    generated_urls = []
    semrush_template = "https://www.semrush.com/analytics/organic/positions/?db=us&q={domain}"
    for domain in domains:
        variations = try_variations(domain)
        for variation in variations:
            if '/' in variation:
                url = f"https://{variation}"
            else:
                url = variation
            semrush_url = semrush_template.format(domain=url)
            generated_urls.append(semrush_url)

def open_urls():
    for url in generated_urls:
        webbrowser.open(url)
        time.sleep(2)

@app.route('/')
def index():
    return render_template('index.html', domains=domains, generated_urls=generated_urls)

@app.route('/update_domains', methods=['POST'])
def update_domains():
    global domains
    domain_input = request.json.get('domains', '')
    domains = [d.strip() for d in domain_input.split(',') if d.strip()]
    generate_semrush_urls()
    return jsonify({
        "success": True,
        "domains": domains,
        "generated_urls": generated_urls,
        "count": len(domains)
    })

@app.route('/open_urls', methods=['POST'])
def trigger_open_urls():
    Thread(target=open_urls).start()
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)