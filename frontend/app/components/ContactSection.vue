<script setup>
import { computed } from 'vue'

const props = defineProps({
  pubications: {
    type: Array,
    default: () => []
  },
  email: {
    type: String,
    default: ''
  }
})

const sortedPublications = computed(() => {
  return [...props.pubications].sort((a, b) => (a.order_index ?? 0) - (b.order_index ?? 0))
})
</script>

<template>
  <section class="contact-section" id="contact">
    <div class="contact-container">

      <div class="contact-grid">

        <!-- LEFT: Publications -->
        <div class="contact-left">
          <h2>Publications & References</h2>

          <div class="publications-list">
            <div
              v-for="(pub, index) in sortedPublications"
              :key="pub.id"
              class="publication-item"
            >
              <span class="publication-index">[{{ index + 1 }}]</span>

              <p class="publication-text">
                <span v-if="pub.authors" class="publication-author"> {{ pub.authors }}</span>
                "{{ pub.title }}"
                <span class="publication-desc">{{ pub.description }}</span>
                <span v-if="pub.year">, {{ pub.year }}</span>
                
              </p>
            </div>
          </div>
        </div>

        <!-- RIGHT: Contact box -->
        <div class="contact-right">
          <div class="contact-card">
            <h3>Parlons Recherche</h3>

            <p>
              I am open to academic collaborations, discussions about GNNs, GenIA, LLM or other career opportunities in deep learning.
            </p>

            <a
              :href="`mailto:${props.email}?subject=Contact from your portfolio&body=Hello, I would like to discuss...`"
              class="contact-button"
            >
              GET IN TOUCH + 
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>
</template>

<style scoped>
.contact-section {
  padding: var(--space-section-y) var(--space-section-x);
  background: var(--color-bg);
  overflow-x: hidden;
}

.contact-container {
  max-width: var(--container-width);
  margin: 0 auto;
  min-width: 0;
}

.contact-grid {
  background: var(--color-primary);
  border-radius: var(--radius-lg);
  padding: 50px;
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 40px;
  color: white;
  box-sizing: border-box;
}

.contact-left,
.contact-right {
  min-width: 0;
}

.contact-left h2 {
  margin: 0 0 24px;
  font-size: 2rem;
}

.publications-list {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.publication-item {
  display: flex;
  gap: 10px;
  font-size: 0.95rem;
  line-height: 1.6;
  align-items: flex-start;
}

.publication-index {
  opacity: 0.8;
}


.publication-author {
  opacity: 0.8;
  color: black;
}

.publication-text {
  margin: 0;
  min-width: 0;
  overflow-wrap: anywhere;
  word-break: break-word;
}


.publication-desc {
  opacity: 0.9;
}

.contact-right {
  display: flex;
  align-items: center;
}

.contact-card {
  background: rgba(255, 255, 255, 0.08);
  padding: 28px;
  border-radius: var(--radius-md);
}

.contact-card h3 {
  margin: 0 0 12px;
  font-size: 1.3rem;
}

.contact-card p {
  margin: 0 0 20px;
  font-size: 0.95rem;
  opacity: 0.9;
}

.contact-button {
  text-decoration: none;
  font-weight: 600;
  color: white;
  letter-spacing: 0.05em;
}

.contact-button:hover {
  text-decoration: underline;
}

@media (max-width: 900px) {
  .contact-section {
    padding-left: 16px;
    padding-right: 16px;
  }

  .contact-grid {
    grid-template-columns: 1fr;
    padding: 24px 20px;
    gap: 28px;
  }

  .contact-left h2 {
    font-size: 1.8rem;
    line-height: 1.05;
  }

  .publication-item {
    gap: 8px;
    font-size: 0.92rem;
  }

  .contact-card {
    padding: 22px 18px;
  }
}
</style>
