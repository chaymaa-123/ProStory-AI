'use client'

import { Card } from '@/components/ui/card'
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts'

interface PerceptionScoreCardProps {
  positive: number
  neutral: number
  negative: number
  title?: string
  showLegend?: boolean
}

export function PerceptionScoreCard({
  positive,
  neutral,
  negative,
  title = 'Overall Perception',
  showLegend = true,
}: PerceptionScoreCardProps) {
  const data = [
    { name: 'Positive', value: positive, color: 'oklch(0.65 0.12 150)' },
    { name: 'Neutral', value: neutral, color: 'oklch(0.94 0.01 265)' },
    { name: 'Negative', value: negative, color: 'oklch(0.63 0.18 25)' },
  ]

  const total = positive + neutral + negative
  const percentages = data.map((item) => ({
    ...item,
    percentage: total > 0 ? Math.round((item.value / total) * 100) : 0,
  }))

  return (
    <Card className="p-6">
      <div className="mb-6">
        <h3 className="font-semibold text-lg text-foreground mb-2">
          {title}
        </h3>
        <p className="text-sm text-muted-foreground">
          Based on {total} total mentions
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        {percentages.map((item) => (
          <div
            key={item.name}
            className="p-4 rounded-lg border border-border bg-muted/30"
          >
            <div className="flex items-center gap-2 mb-2">
              <div
                className="w-3 h-3 rounded-full"
                style={{ backgroundColor: item.color }}
              />
              <span className="text-sm font-medium text-foreground">
                {item.name}
              </span>
            </div>
            <div className="text-2xl font-bold text-foreground">
              {item.percentage}%
            </div>
            <p className="text-xs text-muted-foreground">
              {item.value} mentions
            </p>
          </div>
        ))}
      </div>

      {total > 0 && (
        <div className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={percentages}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percentage }) => `${name} ${percentage}%`}
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                {percentages.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip formatter={(value) => `${value} mentions`} />
              {showLegend && <Legend />}
            </PieChart>
          </ResponsiveContainer>
        </div>
      )}
    </Card>
  )
}
