'use client'

import { Card } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { TrendingUp, TrendingDown } from 'lucide-react'

interface Theme {
  name: string
  count: number
  trend?: 'up' | 'down' | 'stable'
}

interface KeyThemesCardProps {
  positiveThemes: Theme[]
  negativeThemes: Theme[]
}

export function KeyThemesCard({
  positiveThemes,
  negativeThemes,
}: KeyThemesCardProps) {
  const ThemeItem = ({
    theme,
    sentiment,
  }: {
    theme: Theme
    sentiment: 'positive' | 'negative'
  }) => {
    const bgColor =
      sentiment === 'positive'
        ? 'bg-green-50 dark:bg-green-950/30'
        : 'bg-red-50 dark:bg-red-950/30'
    const textColor =
      sentiment === 'positive'
        ? 'text-green-700 dark:text-green-300'
        : 'text-red-700 dark:text-red-300'
    const borderColor =
      sentiment === 'positive'
        ? 'border-green-200 dark:border-green-800'
        : 'border-red-200 dark:border-red-800'

    return (
      <div
        className={`flex items-center justify-between p-3 rounded-lg border ${borderColor} ${bgColor}`}
      >
        <div className="flex items-center gap-3 flex-1">
          <span className={`text-sm font-medium ${textColor}`}>
            {theme.name}
          </span>
        </div>
        <div className="flex items-center gap-2 flex-shrink-0 ml-2">
          <span className={`text-sm font-semibold ${textColor}`}>
            {theme.count}
          </span>
          {theme.trend === 'up' && (
            <TrendingUp className="w-4 h-4 text-green-600 dark:text-green-400" />
          )}
          {theme.trend === 'down' && (
            <TrendingDown className="w-4 h-4 text-red-600 dark:text-red-400" />
          )}
        </div>
      </div>
    )
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
      {/* Positive Themes */}
      <Card className="p-6">
        <h3 className="font-semibold text-lg text-foreground mb-4 flex items-center gap-2">
          <span className="w-3 h-3 rounded-full bg-green-500" />
          Positive Themes
        </h3>
        <div className="space-y-3">
          {positiveThemes.length > 0 ? (
            positiveThemes.map((theme) => (
              <ThemeItem
                key={theme.name}
                theme={theme}
                sentiment="positive"
              />
            ))
          ) : (
            <p className="text-sm text-muted-foreground text-center py-8">
              No positive themes yet
            </p>
          )}
        </div>
      </Card>

      {/* Negative Themes */}
      <Card className="p-6">
        <h3 className="font-semibold text-lg text-foreground mb-4 flex items-center gap-2">
          <span className="w-3 h-3 rounded-full bg-red-500" />
          Negative Themes
        </h3>
        <div className="space-y-3">
          {negativeThemes.length > 0 ? (
            negativeThemes.map((theme) => (
              <ThemeItem
                key={theme.name}
                theme={theme}
                sentiment="negative"
              />
            ))
          ) : (
            <p className="text-sm text-muted-foreground text-center py-8">
              No negative themes yet
            </p>
          )}
        </div>
      </Card>
    </div>
  )
}
