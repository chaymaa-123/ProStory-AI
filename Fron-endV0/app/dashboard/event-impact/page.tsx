'use client'

import { Navigation } from '@/components/Navigation'
import { DashboardLayout } from '@/components/DashboardLayout'
import { Card } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts'
import { useState } from 'react'
import { ArrowUp, ArrowDown } from 'lucide-react'

const events = [
  'Tech Summit 2024',
  'Leadership Workshop',
  'Career Growth Webinar',
]

const impactData = [
  { metric: 'Positive', before: 45, after: 72, change: '+60%' },
  { metric: 'Neutral', before: 30, after: 18, change: '-40%' },
  { metric: 'Negative', before: 12, after: 5, change: '-58%' },
]

export default function EventImpactPage() {
  const [selectedEvent, setSelectedEvent] = useState(events[0])

  return (
    <main className="min-h-screen bg-background">
      <Navigation currentPath="/dashboard" />

      <DashboardLayout currentSection="event-impact">
        <div className="p-8 space-y-8">
          {/* Header */}
          <div>
            <h1 className="text-3xl font-bold text-foreground mb-2">
              Event Impact
            </h1>
            <p className="text-muted-foreground">
              See how specific events affected your company&apos;s perception
            </p>
          </div>

          {/* Event selector */}
          <div>
            <label className="block text-sm font-semibold text-foreground mb-3">
              Select Event
            </label>
            <select
              value={selectedEvent}
              onChange={(e) => setSelectedEvent(e.target.value)}
              className="w-full md:w-64 px-4 py-2 border border-border rounded-lg bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-primary/50"
            >
              {events.map((event) => (
                <option key={event} value={event}>
                  {event}
                </option>
              ))}
            </select>
          </div>

          {/* Impact comparison */}
          <Card className="p-6">
            <h3 className="font-semibold text-lg text-foreground mb-6">
              Perception Before vs After
            </h3>

            <div className="h-80">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={impactData}>
                  <CartesianGrid
                    strokeDasharray="3 3"
                    stroke="oklch(0.9 0.01 265)"
                  />
                  <XAxis
                    dataKey="metric"
                    stroke="oklch(0.48 0.02 265)"
                    style={{ fontSize: '12px' }}
                  />
                  <YAxis
                    stroke="oklch(0.48 0.02 265)"
                    style={{ fontSize: '12px' }}
                  />
                  <Tooltip
                    contentStyle={{
                      backgroundColor: 'oklch(1 0 0)',
                      border: '1px solid oklch(0.9 0.01 265)',
                      borderRadius: '8px',
                    }}
                  />
                  <Legend wrapperStyle={{ paddingTop: '20px' }} />
                  <Bar dataKey="before" fill="oklch(0.72 0.18 70)" name="Before" />
                  <Bar dataKey="after" fill="oklch(0.65 0.12 150)" name="After" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </Card>

          {/* Change metrics */}
          <div className="grid md:grid-cols-3 gap-6">
            {impactData.map((item) => (
              <Card key={item.metric} className="p-6">
                <p className="text-sm text-muted-foreground mb-2">
                  {item.metric}
                </p>
                <div className="space-y-2">
                  <div className="flex items-baseline gap-2">
                    <span className="text-2xl font-bold text-foreground">
                      {item.after}
                    </span>
                    <span className="text-xs text-muted-foreground">
                      (from {item.before})
                    </span>
                  </div>
                  <div className="flex items-center gap-2">
                    {item.change.startsWith('+') ? (
                      <ArrowUp className="w-4 h-4 text-green-500" />
                    ) : (
                      <ArrowDown className="w-4 h-4 text-green-500" />
                    )}
                    <Badge
                      variant="outline"
                      className="bg-green-100 text-green-800 dark:bg-green-900/40 dark:text-green-300"
                    >
                      {item.change}
                    </Badge>
                  </div>
                </div>
              </Card>
            ))}
          </div>

          {/* Related experiences */}
          <Card className="p-6">
            <h3 className="font-semibold text-lg text-foreground mb-4">
              Related Experiences
            </h3>
            <p className="text-sm text-muted-foreground">
              {selectedEvent} was mentioned in 48 experiences, with an average
              sentiment shift of +32%.
            </p>

            <div className="mt-4 space-y-2">
              <div className="flex items-center justify-between text-sm p-3 bg-green-50 dark:bg-green-950/30 rounded-lg border border-green-200 dark:border-green-800">
                <span className="text-green-800 dark:text-green-300">
                  "Great opportunity to network with industry leaders"
                </span>
                <Badge variant="secondary">+15%</Badge>
              </div>
              <div className="flex items-center justify-between text-sm p-3 bg-green-50 dark:bg-green-950/30 rounded-lg border border-green-200 dark:border-green-800">
                <span className="text-green-800 dark:text-green-300">
                  "Learned valuable insights from keynote speakers"
                </span>
                <Badge variant="secondary">+12%</Badge>
              </div>
            </div>
          </Card>
        </div>
      </DashboardLayout>
    </main>
  )
}
