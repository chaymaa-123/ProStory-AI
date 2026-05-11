'use client'

import { useState, useEffect } from 'react'
import { Navigation } from '@/components/Navigation'
import { DashboardLayout } from '@/components/DashboardLayout'
import { KeyThemesCard } from '@/components/KeyThemesCard'
import { Card } from '@/components/ui/card'
import { api } from '@/lib/api'

interface Theme {
  name: string
  count: number
  trend: 'up' | 'down' | 'stable'
}

interface CompanyInsights {
  company_id: string
  total: number
  positive: number
  neutral: number
  negative: number
  dominant_sentiment: string
  keywords: Array<[string, number]>
  summary: string
  confidence: string
  analysis_timestamp: string
}

export default function InsightsPage() {
  const [insights, setInsights] = useState<CompanyInsights | null>(null)
  const [loading, setLoading] = useState(true)
  const [companyId] = useState('17ef1c45-e07a-48f2-bb6d-c1621015e32f') // TechNova Solutions Seeded ID

  useEffect(() => {
    fetchCompanyThemes()
  }, [])

  const fetchCompanyThemes = async () => {
    try {
      setLoading(true)
      const response = await api.get(`/api/ai/company/${companyId}/insights`)
      setInsights(response.data)
    } catch (error) {
      console.error('Failed to fetch company insights', error)
    } finally {
      setLoading(false)
    }
  }

  // Mapper les keywords du backend aux thèmes
  const allThemes: Theme[] = (insights?.keywords || []).map(([name, count]) => ({
    name,
    count,
    trend: 'stable' as const
  }))

  // Répartition simplifiée pour la démo
  const positiveThemes = allThemes.slice(0, 5)
  const negativeThemes = allThemes.slice(5, 8)

  if (loading) {
    return (
      <main className="min-h-screen bg-background">
        <Navigation currentPath="/dashboard" />
        <DashboardLayout currentSection="insights">
          <div className="p-8">
            <div className="text-center">Chargement des thèmes...</div>
          </div>
        </DashboardLayout>
      </main>
    )
  }

  return (
    <main className="min-h-screen bg-background">
      <Navigation currentPath="/dashboard" />

      <DashboardLayout currentSection="insights">
        <div className="p-8 space-y-8">
          {/* Header */}
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-2">
              Insights
            </h1>
            <p className="text-muted-foreground">
              Explore the key themes mentioned in experiences about your company
            </p>
          </div>

          {/* Themes */}
          <KeyThemesCard
            positiveThemes={positiveThemes}
            negativeThemes={negativeThemes}
          />

          {/* Theme explanation */}
          <Card className="p-6 bg-muted/30">
            <h3 className="font-semibold text-foreground mb-3">
              How we identify themes
            </h3>
            <p className="text-sm text-muted-foreground leading-relaxed">
              Our AI analyzes all experiences shared about your company to identify recurring topics and themes. Themes are categorized as positive or negative based on the sentiment context in which they appear. Arrows indicate whether mentions are increasing (↑), decreasing (↓), or stable (→) over the last 30 days.
            </p>
          </Card>
          {/* Theme statistics */}
          <div className="grid md:grid-cols-3 gap-6">
            <Card className="p-6">
              <p className="text-sm text-muted-foreground mb-1">
                Total Unique Themes
              </p>
              <p className="text-3xl font-bold text-foreground">
                {insights?.keyword_count || allThemes.length}
              </p>
            </Card>

            <Card className="p-6">
              <p className="text-sm text-muted-foreground mb-1">
                Positive Themes
              </p>
              <p className="text-3xl font-bold text-green-600 dark:text-green-400">
                {positiveThemes.length}
              </p>
            </Card>

            <Card className="p-6">
              <p className="text-sm text-muted-foreground mb-1">
                Negative Themes
              </p>
              <p className="text-3xl font-bold text-red-600 dark:text-red-400">
                {negativeThemes.length}
              </p>
            </Card>
          </div>
        </div>
      </DashboardLayout>
    </main>
  )
}
