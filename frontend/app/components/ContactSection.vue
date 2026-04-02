<script setup>
import { computed } from 'vue'

const props = defineProps({
  pubications: {
    type: Array,
    default: () => []
  }
})

const sortedPublications = computed(() => {
  return [...props.pubications].sort((a, b) => (a.order_index ?? 0) - (b.order_index ?? 0))
})
</script>

<template>
  <section class="contact-section">
    <div class="contact-container">

      <div class="contact-grid">

        <!-- LEFT: Publications -->
        <div class="contact-left">
          <h2>Publications & Références</h2>

          <div class="publications-list">
            <div
              v-for="(pub, index) in sortedPublications"
              :key="pub.id"
              class="publication-item"
            >
              <span class="publication-index">[{{ index + 1 }}]</span>

              <p class="publication-text">
                "{{ pub.title }}"<br />
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
              Je suis ouvert aux collaborations académiques, aux échanges sur les GNN
              ou aux opportunités de carrière en Deep Learning.
            </p>

            <a href="#" class="contact-button">
              REPRENDRE CONTACT +
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
}

.contact-container {
  max-width: var(--container-width);
  margin: 0 auto;
}

.contact-grid {
  background: var(--color-primary);
  border-radius: var(--radius-lg);
  padding: 50px;
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 40px;
  color: white;
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
}

.publication-index {
  opacity: 0.8;
}

.publication-text {
  margin: 0;
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
  .contact-grid {
    grid-template-columns: 1fr;
  }
}
</style>
