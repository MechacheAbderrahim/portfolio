

<script setup>
import { computed } from 'vue'

const props = defineProps({
  education: {
    type: Array,
    default: () => []
  }
})

const sortedEducation = computed(() => {
  return [...props.education].sort((a, b) => (a.order_index ?? 0) - (b.order_index ?? 0))
})

const formatYear = (date) => {
  if (!date) return ''
  return new Date(date).getFullYear()
}

const formatDateRange = (start, end) => {
  const startYear = formatYear(start)
  const endYear = end ? formatYear(end) : 'Until now'

  if (startYear === endYear) return startYear
  return `${startYear} - ${endYear}`
}
</script>

<template>
  <section class="education-section" id="education">
    <div class="education-container">

      <h2 class="section-title">Formations</h2>

      <div class="education-list">
        <div
          v-for="item in sortedEducation"
          :key="item.id"
          class="education-item"
        >

          <div class="education-left">
            <span class="education-dot"></span>
            <span class="education-date">
              {{ formatDateRange(item.start_date, item.end_date) }}
            </span>
          </div>

          <div class="education-content">
            <p class="education-institution">
              {{ item.institution }}
              <span v-if="item.rank_info">({{ item.rank_info }})</span>
            </p>

            <h3 class="education-title">
              {{ item.degree }} - {{ item.field }}
            </h3>

            <p class="education-description" v-if="item.description">
              {{ item.description }}
            </p>
          </div>

        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
.education-section {
  padding: var(--space-section-y) var(--space-section-x);
  background: var(--color-bg);
}

.education-container {
  max-width: var(--container-width);
  margin: 0 auto;
}

.section-title {
  font-size: 2.2rem;
  margin-bottom: 40px;
  color: var(--color-text);
}

.education-list {
  display: flex;
  flex-direction: column;
  gap: 40px;
  position: relative;
}

.education-item {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 30px;
}

.education-left {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--color-muted);
}

.education-dot {
  width: 8px;
  height: 8px;
  background: var(--color-primary);
  border-radius: 50%;
}

.education-date {
  font-size: 0.9rem;
  letter-spacing: 0.08em;
}

.education-institution {
  margin: 0;
  font-size: 0.9rem;
  color: var(--color-muted);
}

.education-title {
  margin: 6px 0 10px;
  font-size: 1.5rem;
  color: var(--color-primary);
  font-weight: 500;
}

.education-description {
  margin-top: 6px;
  color: var(--color-muted);
  font-size: 0.95rem;
}

@media (max-width: 900px) {
  .education-item {
    grid-template-columns: 1fr;
  }
}
</style>