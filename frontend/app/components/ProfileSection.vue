<script setup>
import { computed } from 'vue'

const props = defineProps({
  profiles: {
    type: Array,
    default: () => []
  }
})

const profile = computed(() => props.profiles?.[0] || null)

const profileImageUrl = computed(() => {
  if (!profile.value) return '/images/profile.jpg'

  return (
    profile.value.photo_url ||
    profile.value.image_url ||
    profile.value.picture ||
    profile.value.avatar ||
    '/images/profile.jpg'
  )
})

const linkedinUrl = computed(() => {
  if (!profile.value) return '#'
  return profile.value.linkedin_url || profile.value.linkedin || '#'
})

const cvUrl = computed(() => {
  if (!profile.value) return '/abderrahim_mechache_cv.pdf'
  return profile.value.cv_url || profile.value.cv || '/abderrahim_mechache_cv.pdf'
})

const academicUrl = computed(() => {
  if (!profile.value) return '#'
  return (
    profile.value.academic_url ||
    profile.value.google_scholar_url ||
    profile.value.scholar_url ||
    '#'
  )
})

const description = computed(() => {
  if (!profile.value) return ''

  return (
    profile.value.description ||
    profile.value.bio ||
    profile.value.about ||
    profile.value.summary ||
    `Research focused on ${profile.value.subtitle || profile.value.title || 'computer science'}.`
  )
})
</script>

<template>
  <section id="home">
    <div v-if="profile">

      <div>
        <div>
          <h1>{{ profile.full_name }}</h1>
          <p>{{ profile.title }}  |  {{ profile.location }}</p>
          <p>{{ description }}</p>
          <p>Email: {{ profile.email }}</p>
          <p>Location: </p>

          <div>
            <a :href="linkedinUrl" target="_blank" rel="noopener noreferrer">
              LinkedIn Profile
            </a>
            <a :href="academicUrl" target="_blank" rel="noopener noreferrer">
              Academic Profile
            </a>
            <a :href="cvUrl" target="_blank" rel="noopener noreferrer">
              CV
            </a>
          </div>
        </div>

        <div>
          <img :src="profileImageUrl" :alt="profile.full_name" />
        </div>
      </div>
    </div>

    <div v-else>
      <p>Aucun profil trouvé</p>
    </div>
  </section>
</template>

<style scoped>
#home {
  padding: var(--space-section-y) var(--space-section-x);
  overflow-x: hidden;
  background: var(--color-bg);
}

#home > div {
  max-width: var(--container-width);
  margin: 0 auto;
  width: 100%;
  padding: 40px;
  box-sizing: border-box;
}

#home > div > div:first-child {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(320px, 430px);
  align-items: center;
  gap: 72px;
}

/* Bloc texte */
#home > div > div:first-child > div:first-child {
  max-width: 640px;
  width: 100%;
}

#home h1 {
  margin: 0;
  font-size: clamp(3.8rem, 7vw, 5.8rem);
  line-height: 0.92;
  letter-spacing: -0.05em;
  color: var(--color-text);
  font-weight: 400;
}

/* title */
#home > div > div:first-child > div:first-child > p:nth-of-type(1) {
  margin: 24px 0 0;
  font-size: 1.55rem;
  line-height: 1.35;
  color: var(--color-primary);
  font-style: italic;
}

/* description */
#home > div > div:first-child > div:first-child > p:nth-of-type(2) {
  margin: 18px 0 0;
  max-width: 560px;
  font-size: 1.02rem;
  line-height: 1.85;
  color: var(--color-muted);
}

/* cacher email/location */
#home > div > div:first-child > div:first-child > p:nth-of-type(3),
#home > div > div:first-child > div:first-child > p:nth-of-type(4) {
  display: none;
}

/* boutons */
#home > div > div:first-child > div:first-child > div {
  margin-top: 28px;
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}

#home a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0 18px;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: 0.2s ease;

  /* 🔥 MODIF demandée */
  background: var(--color-primary);
  color: #fff; /* texte noir */
  font-style:oblique;
}

#home a:hover {
  opacity: 0.95;
  transform: translateY(-1px);
}

/* image */
#home > div > div:first-child > div:last-child {
  display: flex;
  justify-content: flex-end;
}

#home img {
  display: block;
  width: 100%;
  max-width: 410px;
  aspect-ratio: 4 / 5;
  object-fit: cover;
  border-radius: 2px;
}

/* responsive */
@media (max-width: 980px) {
  #home {
    padding: 56px 16px 40px;
  }

  #home > div {
    padding: 0;
  }

  #home > div > div:first-child {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  #home > div > div:first-child > div:first-child {
    max-width: 100%;
    text-align: center;
  }

  #home h1 {
    font-size: clamp(2.9rem, 14vw, 4.4rem);
    line-height: 0.95;
  }

  #home > div > div:first-child > div:first-child > p:nth-of-type(1),
  #home > div > div:first-child > div:first-child > p:nth-of-type(2) {
    max-width: 100%;
  }

  #home > div > div:first-child > div:first-child > div {
    justify-content: center;
  }

  #home > div > div:first-child > div:last-child {
    justify-content: center;
  }

  #home img {
    max-width: 100%;
  }
}
</style>