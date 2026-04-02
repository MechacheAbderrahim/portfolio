
<script setup>
import { computed } from 'vue'

const config = useRuntimeConfig()
const base = config.public.apiBase

const { data: profileData } = await useFetch(`${base}/profiles`)

const profile = computed(() => profileData.value?.[0] || null)
</script>


<template>
  <div class="layout-shell">
    <header class="site-header">
      <div class="header-inner">
        <a href="#home" class="site-brand">Call Me Rahim !</a>

        <nav class="site-nav" aria-label="Main navigation">
          <a href="#home" class="nav-link nav-link-active">Home</a>
          <a href="#education" class="nav-link">Education</a>
          <a href="#experience" class="nav-link">Experience & Projects</a>
          <a href="#skills" class="nav-link">Skills</a>
          <a href="#contact" class="nav-link">Contact</a>
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