

<script setup>
import { computed } from 'vue'

const props = defineProps({
  skills: {
    type: Array,
    default: () => []
  },
  technologies: {
    type: Array,
    default: () => []
  },
  languages: {
    type: Array,
    default: () => []
  }
})

const sortedSkills = computed(() => {
  return [...props.skills]
    .filter(skill => skill.display)
    .sort((a, b) => a.name.localeCompare(b.name))
})

const sortedTechnologies = computed(() => {
  return [...props.technologies].sort((a, b) => a.name.localeCompare(b.name))
})

const sortedLanguages = computed(() => {
  return [...props.languages].sort((a, b) => {
    return (a.order_index ?? 9999) - (b.order_index ?? 9999)
  })
})

const getLanguageWidth = (level) => {
  const normalized = (level || '').toLowerCase()

  if (normalized === 'native') return '100%'
  if (normalized === 'fluent') return '92%'
  if (normalized === 'advanced') return '85%'
  if (normalized === 'intermediate') return '75%'
  if (normalized === 'basic') return '45%'

  return '60%'
}
</script>

<template>
  <section class="skills-section" id="skills">
    <div class="skills-container">
      <div class="skills-heading">
        <h2>Expertise Technique</h2>
        <div class="skills-divider"></div>
      </div>

      <div class="skills-grid">
        <div class="skills-column">
          <h3>Areas of Interest</h3>

          <ul v-if="sortedSkills.length" class="skills-list">
            <li v-for="skill in sortedSkills" :key="skill.id" class="skills-list-item">
              <span class="skills-dot"></span>
              <span>{{ skill.name }}</span>
            </li>
          </ul>

          <p v-else class="skills-empty">No skills found.</p>
        </div>

        <div class="skills-column">
          <h3>Programming &amp; Tools</h3>

          <div v-if="sortedTechnologies.length" class="tech-tags">
            <span v-for="tech in sortedTechnologies" :key="tech.id" class="tech-tag">
              {{ tech.name }}
            </span>
          </div>

          <p v-else class="skills-empty">No technologies found.</p>
        </div>

        <div class="skills-column">
          <h3>Languages</h3>

          <div v-if="sortedLanguages.length" class="languages-list">
            <div v-for="language in sortedLanguages" :key="language.id" class="language-item">
              <div class="language-top">
                <span class="language-name">{{ language.name }}</span>
                <span class="language-level">{{ language.level }}</span>
              </div>

              <div class="language-bar">
                <div class="language-bar-fill" :style="{ width: getLanguageWidth(language.level) }"></div>
              </div>
            </div>
          </div>

          <p v-else class="skills-empty">No languages found.</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.skills-section {
  padding: var(--space-section-y) var(--space-section-x);
  background: var(--color-bg-2);
}

.skills-container {
  max-width: var(--container-width);
  margin: 0 auto;
}

.skills-heading {
  margin-bottom: 52px;
}

.skills-heading h2 {
  margin: 0;
  font-size: 2.8rem;
  line-height: 1.1;
  font-weight: 400;
  color: var(--color-text);
}

.skills-divider {
  width: 96px;
  height: 4px;
  background: var(--color-primary);
  margin-top: 18px;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 48px;
}

.skills-column h3 {
  margin: 0 0 22px;
  padding-bottom: 12px;
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--color-muted);
  border-bottom: 1px solid rgba(31, 41, 55, 0.12);
}

.skills-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.skills-list-item {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--color-text);
  font-size: 1rem;
}

.skills-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-primary);
  flex-shrink: 0;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.tech-tag {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 16px;
  background: #ffffff;
  border: 1px solid rgba(31, 41, 55, 0.12);
  border-radius: var(--radius-md);
  color: var(--color-text);
  font-size: 0.95rem;
}

.languages-list {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.language-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.language-top {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

.language-name {
  color: var(--color-text);
  font-weight: 600;
}

.language-level {
  color: var(--color-muted);
}

.language-bar {
  width: 100%;
  height: 7px;
  background: rgba(31, 41, 55, 0.12);
  border-radius: 999px;
  overflow: hidden;
}

.language-bar-fill {
  height: 100%;
  background: var(--color-primary);
  border-radius: 999px;
}

.skills-empty {
  margin: 0;
  color: var(--color-muted);
}

@media (max-width: 980px) {
  .skills-section {
    padding: 72px 24px 56px;
  }

  .skills-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }
}

@media (max-width: 640px) {
  .skills-section {
    padding: 56px 20px 44px;
  }

  .skills-heading h2 {
    font-size: 2.2rem;
  }
}
</style>