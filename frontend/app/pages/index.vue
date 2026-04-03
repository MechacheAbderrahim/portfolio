<script setup>
const config = useRuntimeConfig()
const base = config.public.apiBase

const { data: profilesData } = await useFetch(`${base}/profiles/`)
const { data: educationData } = await useFetch(`${base}/education/`)
const { data: portfolioData } = await useFetch(`${base}/portfolio/`)
const { data: skillsData } = await useFetch(`${base}/skills/`)
const { data: technologiesData } = await useFetch(`${base}/technologies/`)
const { data: languagesData } = await useFetch(`${base}/languages/`)
const { data: pubicationsData } = await useFetch(`${base}/publications/`)

const profiles = computed(() => profilesData.value || [])
const education = computed(() => educationData.value || [])
const portfolio = computed(() => portfolioData.value || [])
const skills = computed(() => skillsData.value || [])
const technologies = computed(() => technologiesData.value || [])
const languages = computed(() => languagesData.value || [])
const pubications = computed(() => pubicationsData.value || [])
const contactEmail = computed(() => profiles.value?.[0]?.email || '')
</script>

<template>

  <div>
    <ProfileSection :profiles="profiles" />
    <PortfolioSection :portfolio="portfolio" />
    <EducationSection :education="education" />
    <SkillsSection :skills="skills" :technologies="technologies" :languages="languages" />
    <ContactSection :pubications="pubications" :email="contactEmail" />
  </div>
  
</template>