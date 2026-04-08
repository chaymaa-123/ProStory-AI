'use client'

import { Navigation } from '@/components/Navigation'
import { DashboardLayout } from '@/components/DashboardLayout'
import { PerceptionScoreCard } from '@/components/PerceptionScoreCard'
import { TrendChart } from '@/components/TrendChart'
import { AIInsightCard } from '@/components/AIInsightCard'
import { Card } from '@/components/ui/card'
import { TrendingUp, FileText, Eye } from 'lucide-react'

// Mock data
const trendData = [
  { date: 'Mar 1', positive: 45, neutral: 30, negative: 12 },
  { date: 'Mar 8', positive: 52, neutral: 28, negative: 10 },
  { date: 'Mar 15', positive: 58, neutral: 25, negative: 8 },
  { date: 'Mar 22', positive: 62, neutral: 22, negative: 7 },
  { date: 'Mar 29', positive: 67, neutral: 20, negative: 6 },
  { date: 'Apr 5', positive: 72, neutral: 18, negative: 5 },
]

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-background">
      <Navigation currentPath="/dashboard" />

      <DashboardLayout currentSection="overview">
        <div className="p-8 space-y-8">
          {/* Header */}
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-2">
              Dashboard
            </h1>
            <p className="text-muted-foreground">
              Track your company&apos;s perception and insights in real-time
            </p>
          </div>

          {/* Quick Stats */}
          <div className="grid md:grid-cols-3 gap-6">
            <Card className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-muted-foreground mb-1">
                    Total Experiences
                  </p>
                  <p className="text-3xl font-bold text-foreground">247</p>
                </div>
                <FileText className="w-10 h-10 text-accent/50" />
              </div>
            </Card>

            <Card className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-muted-foreground mb-1">
                    Total Views
                  </p>
                  <p className="text-3xl font-bold text-foreground">12.5K</p>
                </div>
                <Eye className="w-10 h-10 text-accent/50" />
              </div>
            </Card>

            <Card className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-muted-foreground mb-1">
                    Positive Trend
                  </p>
                  <p className="text-3xl font-bold text-foreground">↑ 27%</p>
                </div>
                <TrendingUp className="w-10 h-10 text-green-500/50" />
              </div>
            </Card>
          </div>

          {/* AI Insight */}
          <AIInsightCard summary="Your company is perceived as having a strong culture with great career growth opportunities. Employees appreciate the collaborative environment, though some mention that internal communication could be improved." />

          {/* Perception Score */}
          <PerceptionScoreCard
            positive={167}
            neutral={59}
            negative={21}
            title="Overall Perception Score"
          />

          {/* Trend Chart */}
          <TrendChart data={trendData} />

          {/* Bottom CTA */}
          <Card className="p-8 bg-gradient-to-r from-primary/10 to-accent/10 border-primary/20 text-center space-y-4">
            <h3 className="text-2xl font-bold text-foreground">
              Want deeper insights?
            </h3>
            <p className="text-muted-foreground">
              Check out the Insights section to explore themes, or Event Impact to see how specific events affected your perception.
            </p>
          </Card>
        </div>
      </DashboardLayout>
    </main>
  )
}
