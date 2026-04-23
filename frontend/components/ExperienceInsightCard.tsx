'use client'

import { Card } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Brain, TrendingUp, AlertCircle, Minus } from 'lucide-react'

interface ExperienceInsightCardProps {
  sentiment: string
  sentiment_label: string
  sentiment_color: string
  keywords: string[]
  confidence: number
  created_at: string
}

export function ExperienceInsightCard({
  sentiment,
  sentiment_label,
  sentiment_color,
  keywords,
  confidence,
  created_at
}: ExperienceInsightCardProps) {
  const getSentimentIcon = (sentiment: string) => {
    switch (sentiment) {
      case 'positif':
        return <TrendingUp className="w-4 h-4" />
      case 'negatif':
        return <AlertCircle className="w-4 h-4" />
      default:
        return <Minus className="w-4 h-4" />
    }
  }

  const getSentimentColor = (color: string) => {
    switch (color) {
      case 'green':
        return 'bg-green-100 text-green-800 border-green-200'
      case 'red':
        return 'bg-red-100 text-red-800 border-red-200'
      default:
        return 'bg-gray-100 text-gray-800 border-gray-200'
    }
  }

  const getConfidenceLabel = (confidence: number) => {
    if (confidence >= 0.8) return 'Très élevée'
    if (confidence >= 0.6) return 'Élevée'
    if (confidence >= 0.4) return 'Moyenne'
    return 'Faible'
  }

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('fr-FR', {
      day: 'numeric',
      month: 'short',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  return (
    <Card className="p-6 border-dashed border-primary/30 bg-linear-to-br from-primary/5 to-accent/5">
      <div className="flex gap-3">
        <div className="shrink-0 mt-1">
          <Brain className="w-5 h-5 text-primary animate-pulse" />
        </div>
        <div className="flex-1 space-y-4">
          {/* Header */}
          <div className="flex items-center justify-between">
            <h3 className="font-semibold text-lg text-foreground flex items-center gap-2">
              Analyse IA
            </h3>
            <div className="flex items-center gap-2">
              {getSentimentIcon(sentiment)}
              <Badge 
                variant="outline" 
                className={getSentimentColor(sentiment_color)}
              >
                {sentiment_label}
              </Badge>
            </div>
          </div>

          {/* Sentiment Details */}
          <div className="space-y-2">
            <div className="flex justify-between items-center">
              <span className="text-sm text-muted-foreground">Confiance</span>
              <div className="flex items-center gap-2">
                <div className="w-20 bg-gray-200 rounded-full h-2">
                  <div 
                    className="bg-primary h-2 rounded-full transition-all duration-300"
                    style={{ width: `${confidence * 100}%` }}
                  />
                </div>
                <span className="text-xs text-muted-foreground">
                  {getConfidenceLabel(confidence)}
                </span>
              </div>
            </div>
          </div>

          {/* Keywords */}
          {keywords.length > 0 && (
            <div className="space-y-2">
              <h4 className="text-sm font-medium text-foreground">Mots-clés détectés</h4>
              <div className="flex flex-wrap gap-1">
                {keywords.map((keyword, index) => (
                  <Badge 
                    key={index} 
                    variant="secondary" 
                    className="text-xs px-2 py-1"
                  >
                    {keyword}
                  </Badge>
                ))}
              </div>
            </div>
          )}

          {/* Footer */}
          <div className="flex justify-between items-center pt-2 border-t border-border/50">
            <p className="text-xs text-muted-foreground">
              Analyse basée sur le contenu de l'expérience
            </p>
            <span className="text-xs text-muted-foreground">
              {formatDate(created_at)}
            </span>
          </div>
        </div>
      </div>
    </Card>
  )
}
