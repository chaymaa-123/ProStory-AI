'use client'

import { Navigation } from '@/components/Navigation'
import { DashboardLayout } from '@/components/DashboardLayout'
import { KeyThemesCard } from '@/components/KeyThemesCard'
import { Card } from '@/components/ui/card'

export default function InsightsPage() {
  const positiveThemes = [
    { name: 'Company Culture', count: 47, trend: 'up' as const },
    { name: 'Career Growth', count: 42, trend: 'up' as const },
    { name: 'Team Collaboration', count: 35, trend: 'stable' as const },
    { name: 'Work-Life Balance', count: 28, trend: 'up' as const },
    { name: 'Leadership', count: 23, trend: 'stable' as const },
  ]

  const negativeThemes = [
    { name: 'Communication', count: 12, trend: 'down' as const },
    { name: 'Process Clarity', count: 8, trend: 'stable' as const },
    { name: 'Remote Work Limitations', count: 5, trend: 'down' as const },
  ]

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
              <p className="text-3xl font-bold text-foreground">18</p>
            </Card>

            <Card className="p-6">
              <p className="text-sm text-muted-foreground mb-1">
                Positive Themes
              </p>
              <p className="text-3xl font-bold text-green-600 dark:text-green-400">
                12
              </p>
            </Card>

            <Card className="p-6">
              <p className="text-sm text-muted-foreground mb-1">
                Negative Themes
              </p>
              <p className="text-3xl font-bold text-red-600 dark:text-red-400">
                3
              </p>
            </Card>
          </div>
        </div>
      </DashboardLayout>
    </main>
  )
}
