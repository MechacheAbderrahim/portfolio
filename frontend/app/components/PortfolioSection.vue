<script setup>
import { computed } from 'vue'

const props = defineProps({
  portfolio: {
    type: Array,
    default: () => []
  }
})

const sortedPortfolio = computed(() => {
  return [...props.portfolio].sort((a, b) => {
    return (a.order_index ?? 9999) - (b.order_index ?? 9999)
  })
})

const getCategory = (item) => {
  return (
    item.category ||
    item.type ||
    item.context ||
    item.label ||
    'Project'
  )
}

const getLocation = (item) => {
  return item.location || item.place || ''
}

const formatYearRange = (item) => {
  const start = item.start_date ? new Date(item.start_date).getFullYear() : null
  const end = item.end_date ? new Date(item.end_date).getFullYear() : null

  if (start && end) {
    if (start === end) return `${start}` // 🔥 même année
    return `${start} - ${end}`
  }

  if (start && !end) return `${start} - Until now` // 🔥 modif
  if (!start && end) return `${end}`

  return ''
}
</script>

<template>
  <section id="experience" class="portfolio-section">
    <div class="portfolio-container">
      <div class="portfolio-header">
        <h2>Expériences &amp; Projets</h2>
        <p>Recherche, Enseignement et Développement technique</p>
      </div>

      <div v-if="sortedPortfolio.length" class="portfolio-grid">
        <article
          v-for="item in sortedPortfolio"
          :key="item.slug || item.id"
          class="portfolio-card"
        >
          <div class="portfolio-card-top">
            <div class="portfolio-icon">
              <span v-if="formatYearRange(item)">{{ formatYearRange(item) }}</span>
            </div>

            <p class="portfolio-category">
              {{ getCategory(item) }}
            </p>
          </div>

          <h3>{{ item.title }}</h3>

          <p class="portfolio-description">
            {{ item.description }}
          </p>

          <p v-if="getLocation(item)" class="portfolio-location">
            {{ getLocation(item) }}
          </p>

          <div class="portfolio-tags">
            <div v-if="item.skills?.length" class="portfolio-tags-row skills">
                <span v-for="s in item.skills" :key="s" class="portfolio-tag skill">
                {{ typeof s === 'string' ? s : s.name }}
                </span>
            </div>

            <div v-if="item.technologies?.length" class="portfolio-tags-row tech">
                <span v-for="t in item.technologies" :key="t" class="portfolio-tag tech">
                {{ typeof t === 'string' ? t : t.name }}
                </span>
            </div>
            </div>
        </article>
      </div>

      <p v-else class="portfolio-empty">
        Aucun projet trouvé.
      </p>
    </div>
  </section>
</template>

<style scoped>
.portfolio-section {
  padding: var(--space-section-y) var(--space-section-x);
  background: var(--color-bg-2);
}

.portfolio-container {
  max-width: var(--container-width);
  margin: 0 auto;
}

.portfolio-header {
  margin-bottom: 42px;
}

.portfolio-header h2 {
  margin: 0;
  font-size: 2.8rem;
  line-height: 1.1;
  font-weight: 400;
  color: var(--color-text);
}

.portfolio-header p {
  margin: 10px 0 0;
  font-size: 1rem;
  color: var(--color-muted);
}

.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.portfolio-card {
  background: #ffffff;
  padding: 24px 22px 20px;
  min-height: 250px;
  display: flex;
  flex-direction: column;
  border-left: 1px solid transparent;
}

.portfolio-card-featured {
  border-left: 3px solid var(--color-primary);
}

.portfolio-card-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 20px;
}

.portfolio-icon {
  min-width: 70px;
  display: inline-flex;
  align-items: center;
  justify-content: flex-start;
  color: var(--color-primary);
  font-size: 0.72rem;
  font-weight: 600;
  line-height: 1.2;
  flex-shrink: 0;
}

.portfolio-category {
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.65rem;
  color: #9aa1aa;
  text-align: right;
}

.portfolio-card h3 {
  margin: 0 0 14px;
  font-size: 1.95rem;
  line-height: 1.15;
  font-weight: 400;
  color: var(--color-text);
}

.portfolio-description {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.75;
  color: var(--color-muted);
}

.portfolio-location {
  margin: 14px 0 0;
  font-size: 0.8rem;
  color: var(--color-primary);
}

.portfolio-tags {
  margin-top: auto;
  padding-top: 18px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.portfolio-tags-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.portfolio-tag {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 4px 9px;
  font-size: 0.62rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  background: #dfe4ff;
  color: var(--color-primary);
}

.portfolio-tag.skill {
  background: var(--color-primary);
  color: #fff;
  font-size: 10px;
  padding: 8px;
}

.portfolio-tag.tech {
    font-size: 8px;
    padding: 8px;
}
.portfolio-empty {
  margin: 0;
  color: var(--color-muted);
}

@media (max-width: 980px) {
  .portfolio-section {
    padding: 72px 24px;
  }

  .portfolio-grid {
    grid-template-columns: 1fr;
  }

  .portfolio-card h3 {
    font-size: 1.7rem;
  }
}

@media (max-width: 640px) {
  .portfolio-section {
    padding: 56px 20px;
  }

  .portfolio-header h2 {
    font-size: 2.2rem;
  }

  .portfolio-card {
    padding: 20px 18px;
  }
}
</style>