
services = [
    "Terrace Waterproofing",
    "Basement Waterproofing",
    "Bathroom Waterproofing",
    "Wall Waterproofing",
    "Kitchen Waterproofing",
    "Garden Waterproofing",
    "Roof Waterproofing",
    "Injection Grouting",
    "Guniting Waterproofing",
    "Retaining Wall Waterproofing",
    "APP Membrane Waterproofing",
    "HDPE Membrane Waterproofing"
]

template = """          <div class="col-lg-4" data-aos="fade-up" data-aos-delay="{delay}">
            <div class="service-card">
              <div class="service-icon">
                <i class="bi bi-building"></i>
              </div>
              <h3>{title}</h3>
              <p>Specialized waterproofing solutions for commercial buildings, ensuring long-lasting protection against
                water damage.</p>
              <div class="service-features">
                <span><i class="bi bi-check-circle"></i> Office Buildings</span>
                <span><i class="bi bi-check-circle"></i> Retail Spaces</span>
                <span><i class="bi bi-check-circle"></i> Warehouses</span>
              </div>
              <a href="service-details.html" class="service-link">Learn More <i class="bi bi-arrow-right"></i></a>
            </div>
          </div><!-- End Service Item -->"""

output = []
delay = 100
for i, service in enumerate(services):
    delay += 100
    if delay > 600: delay = 100
    output.append(template.format(title=service, delay=delay))

with open(r"d:\Constructo\services_cards.html", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print("Done writing to d:\\Constructo\\services_cards.html")
