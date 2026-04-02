<script setup>
import { computed, ref, onMounted, onBeforeUnmount } from 'vue'

const config = useRuntimeConfig()
const base = config.public.apiBase

const { data: profileData } = await useFetch(`${base}/profiles`)
const profile = computed(() => profileData.value?.[0] || null)

const activeSection = ref('home')

const navItems = [
  { id: 'home', label: 'Home' },
  { id: 'experience', label: 'Experience & Projects' },
  { id: 'education', label: 'Education' },
  { id: 'skills', label: 'Skills' },
  { id: 'contact', label: 'Contact' }
]

let observer

onMounted(() => {
  const sections = navItems
    .map(item => document.getElementById(item.id))
    .filter(Boolean)

  observer = new IntersectionObserver(
    (entries) => {
      const visibleEntry = entries
        .filter(entry => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0]

      if (visibleEntry) {
        activeSection.value = visibleEntry.target.id
      }
    },
    {
      threshold: 0.35,
      rootMargin: '-10% 0px -45% 0px'
    }
  )

  sections.forEach(section => observer.observe(section))
})

onBeforeUnmount(() => {
  if (observer) observer.disconnect()
})
</script>


<template>
  <div class="layout-shell">
    <header class="site-header">
      <div class="header-inner">
        <a href="#home" class="site-brand">Call Me Rahim !</a>

        <nav class="site-nav" aria-label="Main navigation">
          <a
            v-for="item in navItems"
            :key="item.id"
            :href="`#${item.id}`"
            class="nav-link"
            :class="{ 'nav-link-active': activeSection === item.id }"
          >
            {{ item.label }}
          </a>
        </nav>
      </div>
    </header>

    <main>
      <slot />
    </main>

    <footer class="site-footer">
      <div class="footer-inner">
        <p class="footer-name">Abderrahim Mechache</p>

        <nav class="footer-nav" aria-label="Footer navigation">
          <a href="/abderrahim_mechache_cv.pdf" target="_blank">Curriculum Vitae</a>
          <a v-if="profile?.google_scholar_url" :href="profile.google_scholar_url" target="_blank">Google Scholar</a>
          <a v-if="profile?.github_url" :href="profile.github_url" target="_blank">GitHub</a>
          <a v-if="profile?.linkedin_url" :href="profile.linkedin_url" target="_blank">LinkedIn</a>
        </nav>

        <p class="footer-copy">© 2026 Digital Curator. All Rights Reserved.</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.layout-shell {
  min-height: 100vh;
  background: var(--color-bg);
  color: var(--color-text);
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(17, 24, 39, 0.06);
}

.header-inner {
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 18px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.site-brand {
  text-decoration: none;
  font-size: 1.7rem;
  font-style: italic;
  color: #182c73;
  white-space: nowrap;
}

.site-nav {
  display: flex;
  align-items: center;
  gap: 28px;
}

.nav-link {
  position: relative;
  text-decoration: none;
  font-size: 0.95rem;
  color: #4b5563;
  padding-bottom: 6px;
}

.nav-link:hover {
  color: #182c73;
}

.nav-link-active {
  color: #182c73;
  font-weight: 600;
}

.nav-link-active::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 2px;
  background: #3047d2;
}

.site-footer {
  border-top: 1px solid rgba(17, 24, 39, 0.08);
  background: #f8f9fa;
}

.footer-inner {
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 28px 32px 36px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
}

.footer-name,
.footer-copy {
  margin: 0;
  font-size: 0.9rem;
  color: #4b5563;
}

.footer-nav {
  display: flex;
  align-items: center;
  gap: 24px;
  flex-wrap: wrap;
}

.footer-nav a {
  text-decoration: none;
  font-size: 0.85rem;
  color: #6b7280;
}

.footer-nav a:hover {
  color: #182c73;
}

@media (max-width: 900px) {
  .header-inner,
  .footer-inner {
    padding-left: 20px;
    padding-right: 20px;
  }

  .header-inner {
    flex-direction: column;
    align-items: flex-start;
  }

  .site-nav {
    flex-wrap: wrap;
    gap: 16px;
  }

  .footer-inner {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>