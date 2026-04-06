'use client'

import { Card } from '@/components/ui/card'
import { Sparkles } from 'lucide-react'

interface AIInsightCardProps {
  summary: string
  period?: string
}

export function AIInsightCard({
  summary,
  period = 'This month',
}: AIInsightCardProps) {
  return (
    <Card className="p-6 border-primary/20 bg-gradient-to-br from-primary/5 to-accent/5">
      <div className="flex gap-3">
        <div className="flex-shrink-0 mt-1">
          <Sparkles className="w-5 h-5 text-accent animate-pulse" />
        </div>
        <div className="flex-1">
          <h3 className="font-semibold text-lg text-foreground mb-2 flex items-center gap-2">
            AI Summary
          </h3>
          <div className="space-y-2">
            <p className="text-sm text-muted-foreground leading-relaxed">
              {period}, <span className="font-medium text-foreground">{summary}</span>
            </p>
            <p className="text-xs text-muted-foreground">
              This summary is based on analysis of mentions and sentiment across all experiences shared about your company.
            </p>
          </div>
        </div>
      </div>
    </Card>
  )
}
